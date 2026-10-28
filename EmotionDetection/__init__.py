"""
EmotionDetection package
========================
Public API for the IBM Watson NLP Emotion Detection project.

Usage::

    from EmotionDetection import emotion_detector
    result = emotion_detector("I am so happy today!")
    print(result)
"""

from emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
