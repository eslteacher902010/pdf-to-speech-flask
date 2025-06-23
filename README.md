# 📄 PDF-to-Speech Web App

This Flask web application allows users to upload PDF files and converts the extracted text into speech using Google Text-to-Speech (gTTS). The resulting audio is downloadable in WAV format.

## 🚀 Features

- Upload any `.pdf` file
- Extract text using `PyPDF2`
- Convert extracted text to audio using `gTTS`
- Download or listen to the output as a `.wav` file

## 🧰 Tech Stack

- Python 3
- Flask
- PyPDF2
- gTTS
- pydub
- HTML/CSS (Jinja2 Templates)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eslteacher902010/pdf-to-speech-flask.git
   cd pdf-to-speech-flask
