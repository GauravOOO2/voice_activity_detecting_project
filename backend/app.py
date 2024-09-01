from flask import Flask, request, jsonify
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['audio']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    audio = AudioSegment.from_file(file_path)
    silence_timestamps = detect_silence(audio)

    return jsonify({"vadResults": silence_timestamps})

def detect_silence(audio):
    silence_ranges = detect_nonsilent(audio, min_silence_len=1000, silence_thresh=-40)
    timestamps = [(start / 1000, stop / 1000) for start, stop in silence_ranges]
    return timestamps

if __name__ == '__main__':
    app.run(debug=True)
