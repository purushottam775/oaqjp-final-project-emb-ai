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

REQUEST_TIMEOUT = 15  # seconds

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
    except requests.exceptions.Timeout:
        print("ERROR: Request to Watson NLP timed out.")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to Watson NLP endpoint.")
    except requests.exceptions.RequestException as exc:
        print(f"ERROR: Unexpected request error: {exc}")
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
        print("ERROR: Unexpected Watson NLP response structure.")
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
              input is blank.  Returns ``None`` on unrecoverable errors.

    Example::

        >>> result = emotion_detector("I am so happy today!")
        >>> result['dominant_emotion']
        'joy'
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return dict(_NONE_RESULT)

    response = _post_to_watson({"raw_document": {"text": text_to_analyze}})

    if response is None:
        return None
    if response.status_code == 400:
        return dict(_NONE_RESULT)
    if response.status_code != 200:
        print(f"ERROR: Watson NLP returned HTTP {response.status_code}.")
        return None
    return _parse_response(response)
