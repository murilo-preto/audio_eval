from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory('static/audio', filename)

@app.route('/audio/aac/<filename>')
def serve_audio_aac(filename):
    return send_from_directory('static/audio/aac', filename)

@app.route('/audio/mp3/<filename>')
def serve_audio_mp3(filename):
    return send_from_directory('static/audio/mp3', filename)

@app.route('/audio/ogg/<filename>')
def serve_audio_ogg(filename):
    return send_from_directory('static/audio/ogg', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
