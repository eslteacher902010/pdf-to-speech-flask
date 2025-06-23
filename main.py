from flask import Flask, request, render_template, redirect, url_for, flash
import fitz
import os
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from datetime import datetime

# Get the current date and time
now = datetime.now()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename=file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

    return redirect(url_for('convert', filename=filename))


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    filename=request.args.get('filename')
    if not filename:
        return "No file specified."

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return "File not found."

    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()

    return redirect(url_for('speechify', text=text))

@app.route('/speech', methods=['GET', 'POST'])
def speechify():
    text=request.args.get('text')
    if not text:
        return "No text specified."

    tts = gTTS(text=text, lang='en')

    # Save to a BytesIO object
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Format the datetime object as YYYYMMDD_HHMMSS
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp_str}.wav"

    audio = AudioSegment.from_mp3(mp3_fp)
    audio.export(os.path.join("static", "uploads", filename), format="wav")

    return render_template("speech.html", audio_file=filename)


if __name__ == '__main__':
    app.run(debug=True)








