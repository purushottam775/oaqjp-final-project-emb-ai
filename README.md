<<<<<<< HEAD
# IBM Watson NLP Emotion Detector — Final Project

> **IBM Skills Network · Python Project for AI and Application Development**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green)](https://flask.palletsprojects.com/)
[![PyLint](https://img.shields.io/badge/PyLint-10.00%2F10-brightgreen)](https://pylint.org/)
[![Tests](https://img.shields.io/badge/Tests-15%2F15%20passing-brightgreen)](test_emotion_detection.py)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📋 Project Overview

The **Emotion Detector** is an AI-powered web application that analyses text and identifies five emotions — **anger**, **disgust**, **fear**, **joy**, and **sadness** — using the IBM Watson NLP EmotionPredict API.  
A clean Flask web interface lets users enter any sentence and see real-time emotion scores plus the dominant emotion.

---

## 🎯 Project Objectives

| # | Objective |
|---|-----------|
| 1 | Create a public GitHub repository with a detailed README |
| 2 | Implement the `emotion_detector()` function using IBM Watson NLP |
| 3 | Format the API output into a structured Python dictionary |
| 4 | Package the function as the `EmotionDetection` importable package |
| 5 | Write unit tests using `unittest` with mocked HTTP responses |
| 6 | Build a Flask web application to serve the detector |
| 7 | Implement HTTP 400 and blank-input error handling |
| 8 | Achieve a PyLint score of **10.00/10** on all source files |

---

## 🛠 Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3.9+ | Core language |
| IBM Watson NLP API | Emotion analysis engine |
| `requests` | HTTP client for API calls |
| Flask 3.0+ | Web server framework |
| HTML + CSS | Frontend interface |
| `unittest` + `unittest.mock` | Unit testing with mocked HTTP |
| PyLint | Static code analysis |
| Git + GitHub | Version control |

---

## 📁 Project Structure

```
emotion-detector/
├── README.md                        # This file
├── SUBMISSION_CHECKLIST.md          # Grading criteria evidence map
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
├── emotion_detection.py             # Task 2 & 3 — Core detection logic
├── server.py                        # Task 6 & 7 — Flask web server
├── test_emotion_detection.py        # Task 5 — Unit tests
├── EmotionDetection/
│   └── __init__.py                  # Task 4 — Python package
├── templates/
│   └── index.html                   # Flask HTML template
├── static/
│   └── style.css                    # UI stylesheet
└── screenshots/
    ├── 6b_deployment_test.png       # Task 6 evidence
    └── 7c_error_handling_interface.png  # Task 7 evidence
```

---

## ⚙️ Installation (Windows)

### Prerequisites
- Python 3.9 or later  
- Git

### 1 — Clone the repository

```powershell
git clone https://github.com/purushottam775/emotion-detector.git
cd emotion-detector
```

### 2 — Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **Note:** If PowerShell blocks activation with a script-execution policy error, run the following command in an Administrator PowerShell window **once**, then retry activation:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> Alternatively, invoke Python directly without activating:
> ```powershell
> .\.venv\Scripts\python.exe server.py
> ```

### 3 — Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Running the Emotion Detector

### Verify the package import

```powershell
python -c "from EmotionDetection import emotion_detector; print(callable(emotion_detector))"
```

Expected output:
```
True
```

### Quick function test (command-line)

```powershell
python -c "
from EmotionDetection import emotion_detector
result = emotion_detector('I am so happy today!')
print(result)
"
```

Expected output structure:
```python
{
    'anger': 0.0073...,
    'disgust': 0.0023...,
    'fear': 0.0059...,
    'joy': 0.9669...,
    'sadness': 0.0174...,
    'dominant_emotion': 'joy'
}
```

---

## 🌐 Starting the Flask Web Application

```powershell
python server.py
```

Flask will print:
```
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

Open your browser at **http://127.0.0.1:5000/**  
Type any sentence in the text area and click **Analyse Emotion**.

---

## 🧪 Running Unit Tests

```powershell
python -m unittest -v test_emotion_detection.py
```

Expected output (15 tests):
```
test_dominant_anger ... ok
test_dominant_disgust ... ok
test_dominant_fear ... ok
test_dominant_joy ... ok
test_dominant_sadness ... ok
test_blank_input_returns_none_dominant ... ok
test_connection_error_returns_none ... ok
test_http_400_returns_none_dominant ... ok
test_http_500_returns_none ... ok
test_timeout_returns_none ... ok
test_whitespace_input_returns_none_dominant ... ok
test_all_required_keys_present ... ok
test_dominant_emotion_is_string ... ok
test_emotion_scores_are_numeric ... ok
test_return_type_is_dict ... ok
----------------------------------------------------------------------
Ran 15 tests in 0.004s
OK
```

All tests use **mocked HTTP responses** — no live network connection or API credentials are required.

---

## 🔍 Running PyLint (Static Code Analysis)

```powershell
python -m pylint server.py
python -m pylint emotion_detection.py
python -m pylint test_emotion_detection.py
```

Expected result for each file:
```
------------------------------------
Your code has been rated at 10.00/10
```

---

## 🔑 API Configuration

The IBM Watson NLP endpoint is configured as constants in `emotion_detection.py`:

```python
WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
```

**No API key is required** — the IBM Skills Network endpoint is publicly accessible during the course.

### Troubleshooting

| Problem | Solution |
|---------|---------|
| `ConnectionError` | Check your internet connection; the Watson NLP host must be reachable |
| HTTP 400 response | The API rejected the input — ensure the text is non-empty and in English |
| HTTP 503 from Flask | The Watson NLP service is temporarily unavailable; retry later |
| PyLint not found | Run `pip install pylint` |
| Flask not found | Run `pip install flask` |
| Script cannot be loaded (PowerShell) | See the virtual-environment activation note above |

---

## 📸 Screenshots

| Screenshot | Task | Description |
|-----------|------|-------------|
| `screenshots/6b_deployment_test.png` | Task 6 | Flask app running in browser with emotion analysis result |
| `screenshots/7c_error_handling_interface.png` | Task 7 | Browser showing "Invalid text! Please try again!" error message |

---

## 📚 Assignment Task Mapping

| Task | Description | Key File(s) |
|------|-------------|-------------|
| 1 | Repository and README | `README.md` |
| 2 | Implement emotion detection | `emotion_detection.py` |
| 3 | Format the output | `emotion_detection.py` |
| 4 | Create and validate the package | `EmotionDetection/__init__.py` |
| 5 | Unit testing | `test_emotion_detection.py` |
| 6 | Flask web deployment | `server.py`, `templates/index.html`, `static/style.css` |
| 7 | Error handling | `emotion_detection.py`, `server.py` |
| 8 | Static code analysis | All `.py` files, PyLint |

---

## 🔗 Repository

**GitHub:** https://github.com/purushottam775/emotion-detector

---

## 📄 License

This project is submitted as part of the IBM Skills Network coursework. Source code is provided for educational purposes.
=======
# Repository for final project
>>>>>>> 3e04588b7b73640f1afb806d3e6bf3e2a41e8fd2
