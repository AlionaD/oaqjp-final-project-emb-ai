"""Module for web deployment"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def e_detector():
    """
    Function to analyze emotions from text.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    emotions = ', '.join(f'{key}: {value}' for key, value in response.items() \
    if key != "dominant_emotion")
    dominant_emotion = response.get("dominant_emotion", "None")
    return f"For the given statement, the system response is {emotions}.\
    The dominant emotion is <strong>{dominant_emotion}</strong>."

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
