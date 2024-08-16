import speech_recognition as sr
import os
import pygame

# TODO: Make listen function loop for continuous feedback
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        phrase = recognizer.recognize_google(audio)
        print(f"Recognized phrase: {phrase}")
        wordsInPhrase = phrase.split()

        if wordsInPhrase[0].lower() == "play" and len(wordsInPhrase) > 1:
            song = ' '.join(wordsInPhrase[1:])
            print(song)
            play_song_from_directory(song, "./songs")
            # Wait for the music to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Check every 100ms if the music is still playing
            print(f"Finished playing {song}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def play_song_from_directory(song, directory):
    pygame.mixer.init()
    for file in os.listdir(directory):
        if song.lower() in str(file).lower() and file.endswith('.mp3'):
            mp3_path = os.path.join(directory, file)
            print(f"Now playing: {file}")
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play()

if __name__ == "__main__":
    listen()
