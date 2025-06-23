This project is a desktop-based language translator built using Python. It provides real-time text translation between multiple languages and integrates speech synthesis to read the translated output aloud. The tool features a graphical interface developed with `tkinter`, utilizes `googletrans` for translation, and `gTTS` for converting text to speech.

## Features

- Translate text between over 100 languages
- Listen to the translated text using Google Text-to-Speech
- Copy translated output to the clipboard
- Simple and user-friendly GUI

## Technologies Used

- **Python 3.x**
- **tkinter** – GUI development
- **googletrans** – Free Google Translate API wrapper (unofficial)
- **gTTS** – Google Text-to-Speech
- **playsound** – For playing audio output

## How It Works

1. Enter the text you want to translate in the input field.
2. Select the source and target languages from the dropdowns.
3. Click the **Translate** button to see the translated text.
4. Click **Speak** to hear the translated text aloud.
5. Optionally, use the **Copy** button to copy the output to the clipboard.

## Installation

Before running the application, install the required Python libraries:

```bash
pip install googletrans==4.0.0-rc1 gTTS playsound
