"""
This module is the server file for emotion detector app
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    """
    Takes request query of text to analyze and analyzes with emotion detection package
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    emotions = [(k, v) for k, v in response.items() if k != 'dominant_emotion']

    response_string = ""
    for i, (key, value) in enumerate(emotions):
        if i == len(emotions) - 1:
            response_string += f"and {key}: {value}"
        else:
            response_string += f"{key}: {value}, "
    return (f"For the given statement, the system response is {response_string}."
    f"The dominant emotion is {dominant_emotion}")

@app.route("/")
def homepage():
    """
    Returns homepage
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
