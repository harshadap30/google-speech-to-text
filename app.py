from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    r = sr.Recognizer()

    with sr.AudioFile(request.files['audio'].stream) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language='en')
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == '__main__':
    app.run(debug=True)
