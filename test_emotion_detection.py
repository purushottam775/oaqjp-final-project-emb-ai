"""
test_emotion_detection.py
=========================
Unit tests for the IBM Watson NLP Emotion Detector.

All HTTP calls are mocked — no live network connection is required.

Run with:
    python -m unittest -v test_emotion_detection.py
"""

import unittest
from unittest.mock import patch, MagicMock

import requests as req_lib  # imported at top-level to satisfy pylint

from EmotionDetection import emotion_detector


# ---------------------------------------------------------------------------
# Helpers – realistic Watson NLP response factory
# ---------------------------------------------------------------------------

def _make_watson_response(scores, status=200):
    """Return a mock requests.Response with the given emotion scores.

    Args:
        scores (dict): Mapping of emotion name to score value.
                       Expected keys: anger, disgust, fear, joy, sadness.
        status (int): HTTP status code (default 200).

    Returns:
        MagicMock: A mock response object.
    """
    mock_response = MagicMock()
    mock_response.status_code = status
    mock_response.json.return_value = {
        "emotionPredictions": [{"emotion": scores}]
    }
    return mock_response


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

class TestEmotionDetectorDominance(unittest.TestCase):
    """Verify that each emotion can be correctly identified as dominant."""

    @patch("emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        """Joy should be dominant when its score is highest."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.05, "disgust": 0.02, "fear": 0.03,
             "joy": 0.85, "sadness": 0.05}
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("emotion_detection.requests.post")
    def test_dominant_anger(self, mock_post):
        """Anger should be dominant when its score is highest."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.90, "disgust": 0.10, "fear": 0.05,
             "joy": 0.02, "sadness": 0.08}
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("emotion_detection.requests.post")
    def test_dominant_sadness(self, mock_post):
        """Sadness should be dominant when its score is highest."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.04, "disgust": 0.05, "fear": 0.07,
             "joy": 0.03, "sadness": 0.81}
        )
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("emotion_detection.requests.post")
    def test_dominant_fear(self, mock_post):
        """Fear should be dominant when its score is highest."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.10, "disgust": 0.05, "fear": 0.78,
             "joy": 0.02, "sadness": 0.05}
        )
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("emotion_detection.requests.post")
    def test_dominant_disgust(self, mock_post):
        """Disgust should be dominant when its score is highest."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.10, "disgust": 0.82, "fear": 0.03,
             "joy": 0.02, "sadness": 0.03}
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")


class TestEmotionDetectorOutputFormat(unittest.TestCase):
    """Verify the structure and types of the returned dictionary."""

    @patch("emotion_detection.requests.post")
    def test_return_type_is_dict(self, mock_post):
        """emotion_detector must return a dict."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.1, "disgust": 0.1, "fear": 0.1,
             "joy": 0.6, "sadness": 0.1}
        )
        result = emotion_detector("test")
        self.assertIsInstance(result, dict)

    @patch("emotion_detection.requests.post")
    def test_all_required_keys_present(self, mock_post):
        """Result must contain all six required keys."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.1, "disgust": 0.1, "fear": 0.1,
             "joy": 0.6, "sadness": 0.1}
        )
        result = emotion_detector("test")
        for key in ("anger", "disgust", "fear", "joy", "sadness",
                    "dominant_emotion"):
            self.assertIn(key, result, msg=f"Missing key: {key}")

    @patch("emotion_detection.requests.post")
    def test_emotion_scores_are_numeric(self, mock_post):
        """Emotion scores must be numeric (int or float)."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.2, "disgust": 0.15, "fear": 0.05,
             "joy": 0.50, "sadness": 0.10}
        )
        result = emotion_detector("test")
        for key in ("anger", "disgust", "fear", "joy", "sadness"):
            self.assertIsInstance(
                result[key], (int, float),
                msg=f"{key} score is not numeric"
            )

    @patch("emotion_detection.requests.post")
    def test_dominant_emotion_is_string(self, mock_post):
        """dominant_emotion must be a string."""
        mock_post.return_value = _make_watson_response(
            {"anger": 0.1, "disgust": 0.1, "fear": 0.1,
             "joy": 0.6, "sadness": 0.1}
        )
        result = emotion_detector("test")
        self.assertIsInstance(result["dominant_emotion"], str)


class TestEmotionDetectorErrorHandling(unittest.TestCase):
    """Verify graceful handling of blank input and API errors."""

    def test_blank_input_returns_none_dominant(self):
        """Blank input must return all-None scores without calling the API."""
        result = emotion_detector("")
        self.assertIsNotNone(result)
        self.assertIsNone(result["dominant_emotion"])
        for key in ("anger", "disgust", "fear", "joy", "sadness"):
            self.assertIsNone(result[key])

    def test_whitespace_input_returns_none_dominant(self):
        """Whitespace-only input must return all-None scores."""
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])

    @patch("emotion_detection.requests.post")
    def test_http_400_returns_none_dominant(self, mock_post):
        """HTTP 400 from the API must return all-None scores."""
        mock_400 = MagicMock()
        mock_400.status_code = 400
        mock_post.return_value = mock_400
        result = emotion_detector("some text")
        self.assertIsNotNone(result)
        self.assertIsNone(result["dominant_emotion"])

    @patch("emotion_detection.requests.post")
    def test_http_500_returns_none(self, mock_post):
        """HTTP 500 from the API must return None."""
        mock_500 = MagicMock()
        mock_500.status_code = 500
        mock_post.return_value = mock_500
        result = emotion_detector("some text")
        self.assertIsNone(result)

    @patch("emotion_detection.requests.post")
    def test_connection_error_returns_none(self, mock_post):
        """Network connection failure must return None gracefully."""
        mock_post.side_effect = req_lib.exceptions.ConnectionError("No route")
        result = emotion_detector("some text")
        self.assertIsNone(result)

    @patch("emotion_detection.requests.post")
    def test_timeout_returns_none(self, mock_post):
        """Network timeout must return None gracefully."""
        mock_post.side_effect = req_lib.exceptions.Timeout("Timed out")
        result = emotion_detector("some text")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
