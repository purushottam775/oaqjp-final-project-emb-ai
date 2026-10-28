"""
server.py
=========
Flask web server for the IBM Watson NLP Emotion Detector application.

Run with:
    python server.py

Then open http://127.0.0.1:5000/ in your browser.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main emotion-detector web page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyse the emotion of the submitted text and return a JSON result.

    Query Parameters:
        textToAnalyze (str): The sentence to analyse.

    Returns:
        JSON response with emotion scores and dominant emotion, or an error
        message when the input is blank or the API call fails.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Validate: reject blank input before calling the external API
    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)

    # Handle None result (network/server error) or all-None scores (API 400)
    if result is None:
        return (
            jsonify({"error": "Emotion analysis service is unavailable. "
                               "Please try again later."}),
            503,
        )

    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"result": response_text, "emotions": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
