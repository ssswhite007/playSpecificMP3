from pocketsphinx import LiveSpeech
import os
import pygame

def listen():
    speech = LiveSpeech(buffer_size=4096)
    for phrase in speech:
        print(phrase)
        wordsInPhrase = str(phrase).split()
        if wordsInPhrase[0] == "start" and len(wordsInPhrase) > 1:
            song = ' '.join(wordsInPhrase[1:])
            print(song)
            play_song_from_directory(song, "./songs")
            # Wait for the music to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Check every 100ms if the music is still playing
            print(f"Finished playing {song}")

def play_song_from_directory(song, directory):
    pygame.mixer.init()
    for file in os.listdir(directory):
        if song in str(file).lower() and file.endswith('.mp3'):
            mp3_path = os.path.join(directory, file)
            print(f"Now playing: {file}")
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play()

if __name__ == "__main__":
    listen()