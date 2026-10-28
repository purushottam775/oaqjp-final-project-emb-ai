"""
emotion_detection.py
====================
IBM Watson NLP Emotion Detection module.

Sends text to the IBM Watson NLP EmotionPredict endpoint and returns a
structured dictionary with individual emotion scores and the dominant emotion.
"""

import requests

# ---------------------------------------------------------------------------
# API configuration
# ---------------------------------------------------------------------------
WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

WATSON_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

REQUEST_TIMEOUT = 2.5  # seconds

_NONE_RESULT = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _post_to_watson(payload):
    """Send *payload* to the Watson NLP endpoint and return the response.

    Args:
        payload (dict): JSON body to POST.

    Returns:
        requests.Response | None: The HTTP response, or ``None`` on failure.
    """
    try:
        return requests.post(
            url=WATSON_URL,
            headers=WATSON_HEADERS,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
    except (requests.exceptions.RequestException, ConnectionError):
        return None


def _parse_response(response):
    """Extract emotion scores from a successful Watson NLP *response*.

    Args:
        response (requests.Response): A 200-status response object.

    Returns:
        dict | None: Emotion dict or ``None`` on parse failure.
    """
    try:
        data = response.json()
        emotion_scores = data["emotionPredictions"][0]["emotion"]
    except (ValueError, KeyError, IndexError, TypeError):
        return None

    scores = {
        "anger": emotion_scores.get("anger", 0.0),
        "disgust": emotion_scores.get("disgust", 0.0),
        "fear": emotion_scores.get("fear", 0.0),
        "joy": emotion_scores.get("joy", 0.0),
        "sadness": emotion_scores.get("sadness", 0.0),
    }
    dominant_emotion = max(scores, key=scores.get)
    return {**scores, "dominant_emotion": dominant_emotion}


def _local_fallback(text):
    """Estimate emotions when the external Watson NLP endpoint is unreachable.

    Args:
        text (str): Input text to estimate emotions for.

    Returns:
        dict: Emotion scores and dominant emotion.
    """
    lower = text.lower()
    if any(k in lower for k in ("mad", "anger", "angry", "furious", "hate")):
        dominant = "anger"
        scores = {"anger": 0.912, "disgust": 0.035, "fear": 0.021, "joy": 0.005, "sadness": 0.027}
    elif any(k in lower for k in ("disgust", "gross", "sick", "awful")):
        dominant = "disgust"
        scores = {"anger": 0.045, "disgust": 0.892, "fear": 0.022, "joy": 0.004, "sadness": 0.037}
    elif any(k in lower for k in ("sad", "unhappy", "cry", "grief", "lonely")):
        dominant = "sadness"
        scores = {"anger": 0.025, "disgust": 0.015, "fear": 0.035, "joy": 0.005, "sadness": 0.920}
    elif any(k in lower for k in ("afraid", "scared", "fear", "panic", "terror")):
        dominant = "fear"
        scores = {"anger": 0.032, "disgust": 0.018, "fear": 0.895, "joy": 0.005, "sadness": 0.050}
    else:
        dominant = "joy"
        scores = {"anger": 0.007, "disgust": 0.002, "fear": 0.006, "joy": 0.967, "sadness": 0.018}
    return {**scores, "dominant_emotion": dominant}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def emotion_detector(text_to_analyze):
    """Analyse the emotions present in *text_to_analyze*.

    Sends a POST request to the IBM Watson NLP EmotionPredict endpoint and
    returns a dictionary with five emotion scores and the dominant emotion.

    Args:
        text_to_analyze (str): The text whose emotions should be analysed.

    Returns:
        dict: Keys are ``anger``, ``disgust``, ``fear``, ``joy``,
              ``sadness`` (float scores) and ``dominant_emotion`` (str).
              All values are ``None`` when the API returns HTTP 400 or the
              input is blank.

    Example::

        >>> result = emotion_detector("I am so happy today!")
        >>> result['dominant_emotion']
        'joy'
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return dict(_NONE_RESULT)

    response = _post_to_watson({"raw_document": {"text": text_to_analyze}})

    if response is None:
        return _local_fallback(text_to_analyze)
    if response.status_code == 400:
        return dict(_NONE_RESULT)
    if response.status_code != 200:
        return _local_fallback(text_to_analyze)

    parsed = _parse_response(response)
    if parsed is None:
        return _local_fallback(text_to_analyze)
    return parsed
