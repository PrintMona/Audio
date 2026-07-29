# Audio
# 🎤 Voice-to-Voice AI Assistant
## Project Description
This project implements a Voice-to-Voice AI Assistant using Python. The assistant listens to the user's voice, converts it into text using Whisper, sends the text to the Cohere Large Language Model (LLM) to generate a response, and finally converts the response back into speech using RealtimeTTS.
---
# Project Workflow
The project consists of three main stages:
1. Speech-to-Text (Whisper)
2. LLM Processing (Cohere)
3. Text-to-Speech (RealtimeTTS)
The workflow is illustrated below:

User Speech
↓
Whisper (Speech-to-Text)
↓
Text
↓
Cohere LLM
↓
AI Response
↓
RealtimeTTS
↓
Voice Output
---
# Project Files
## 1. speech_to_text.py
### Purpose
This file records the user's voice through the microphone and converts it into text using the Whisper model.
### How it works
- Loads the Whisper model.
- Records audio from the microphone.
- Saves the recording as input.wav.
- Transcribes the audio into text.
- Displays the recognized text on the terminal.
---
## 2. IIM.py
### Purpose
This file sends the recognized text to the Cohere API.
### How it works
- Reads the API Key from the .env file.
- Connects to the Cohere API.
- Sends the user's text.
- Receives an AI-generated response.
- Prints the response.
---
## 3. text_to_speech.py
### Purpose
Converts the AI response into speech.
### How it works
- Uses RealtimeTTS.
- Uses the Windows System Voice.
- Speaks the generated response through the speakers.
---
## 4. app.py
### Purpose
This is the main file of the project.
### How it works
It combines all previous stages into one application:
1. Records the user's voice.
2. Converts speech to text.
3. Sends the text to Cohere.
4. Receives the AI response.
5. Converts the response into speech.
6. Speaks the response to the user.
---
# Installation
## Step 1
Create a virtual environment
```bash
python -m venv venv
```
---
## Step 2
Activate the environment
Windows
```bash
venv\Scripts\activate
```
---
## Step 3
Install all required packages
```bash
pip install -r requirements.txt
```
---
## Step 4
Install FFmpeg.
Restart the computer after installation.
---
## Step 5
Create a file named:
```
.env
```
Add your Cohere API key:
```text
COHERE_API_KEY=YOUR_API_KEY
```
---
# Required Libraries
- whisper
- torch
- sounddevice
- soundfile
- python-dotenv
- cohere
- RealtimeTTS
- pyttsx3
---
# How to Run
Run the complete assistant using:
```bash
python app.py
```
The assistant will:
1. Wait for your voice.
2. Convert speech to text.
3. Generate an AI response using Cohere.
4. Convert the response to speech.
5. Speak the response aloud.



# Author

Mona
