"""Flask web server for Emotion Detection web application."""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the home page for user input."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """Analyze user input text and return detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is anger: {result['anger']}, "
        f"disgust: {result['disgust']}, fear: {result['fear']}, "
        f"joy: {result['joy']}, sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
