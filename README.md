# Voice-Controlled MP3 Player

This Python program listens for voice commands to play MP3 songs from a specified directory. When the user says "start" followed by the name of a song, the program will search for the song in the `./songs` directory and play it.

## Features

- **Voice Recognition**: Utilizes the `pocketsphinx` library to listen for specific voice commands.
- **MP3 Playback**: Uses `pygame` to handle audio playback of MP3 files.
- **Directory Search**: Automatically searches for the requested song in the specified directory.

## Requirements

- Python 3.x
- `pocketsphinx`: Install via `pip install pocketsphinx`.
- `pygame`: Install via `pip install pygame`.
- A directory named `songs` containing MP3 files to be played.

## Usage

1. **Install the required Python packages**:
   ```bash
   pip install pocketsphinx pygame
   ```

2. **Prepare your songs**:
   - Place your MP3 files in a directory named `songs` located in the same directory as the script.

3. **Run the program**:
   ```bash
   python playSpecificMP3.py
   ```

4. **Give a voice command**:
   - Say `"start"` followed by the name of the song you want to play. For example, `"start NeverGonnaGiveYouUp"` to play a song with "NeverGonnaGiveYouUp" in the filename.

5. **Playback**:
   - The program will find the song in the `./songs` directory and start playing it.
   - It will wait for the song to finish before listening for the next command.

## Example

Assume you have a song named `NeverGonnaGiveYouUp.mp3` in the `./songs` directory. 

- Start the program and say: 
  ```
  start NeverGonnaGiveYouUp
  ```
- The program will search for `NeverGonnaGiveYouUp.mp3`, load it, and begin playback.

## Troubleshooting

- **No song found**: Ensure the song exists in the `./songs` directory and that the name you are saying matches the filename.
- **Playback issues**: Make sure `pygame` is correctly installed and that your MP3 files are not corrupted.

## License

This project is open-source and available under the MIT License.
