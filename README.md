# Final Project

# IBM Watson NLP Emotion Detector

**IBM Skills Network — Python Project for AI and Application Development**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green)](https://flask.palletsprojects.com/)
[![PyLint](https://img.shields.io/badge/PyLint-10.00%2F10-brightgreen)](https://pylint.org/)
[![Tests](https://img.shields.io/badge/Unit%20Tests-unittest-blue)](https://docs.python.org/3/library/unittest.html)

## Project Overview

The Emotion Detector is a Python application that analyzes text using the IBM Watson NLP EmotionPredict API. It identifies five emotions: **anger, disgust, fear, joy, and sadness**.

The application extracts emotion scores, determines the dominant emotion, and displays the results through a Flask web interface.

## Project Objectives

1. Create a GitHub repository with project documentation.
2. Implement an emotion detection function using the Watson NLP library.
3. Format the API response into a Python dictionary.
4. Package the application in the `EmotionDetection` Python package.
5. Create and run unit tests using `unittest`.
6. Deploy the application using Flask.
7. Handle HTTP 400 responses and blank input.
8. Perform static code analysis using PyLint.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.9+ | Application development |
| IBM Watson NLP API | Emotion detection |
| Requests | HTTP requests |
| Flask | Web application |
| HTML and CSS | User interface |
| unittest | Unit testing |
| unittest.mock | Mocking API responses during tests |
| PyLint | Static code analysis |
| Git and GitHub | Version control and repository hosting |

## Project Structure

```text
emotion-detector/
├── README.md
├── SUBMISSION_CHECKLIST.md
├── requirements.txt
├── .gitignore
├── emotion_detection.py
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   └── __init__.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── screenshots/
    ├── 6b_deployment_test.png
    └── 7c_error_handling_interface.png
```

## Installation on Windows

### Prerequisites

- Python 3.9 or later
- Git

### 1. Clone the repository

```powershell
git clone https://github.com/purushottam775/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, run Python directly using `.\.venv\Scripts\python.exe`.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Emotion Detection Implementation

The `emotion_detection.py` module sends text to the Watson NLP EmotionPredict endpoint and extracts the scores for anger, disgust, fear, joy, and sadness.

The function returns a dictionary containing the five scores and the `dominant_emotion` field.

Example of the expected output structure:

```python
{
    'anger': 0.01,
    'disgust': 0.01,
    'fear': 0.02,
    'joy': 0.90,
    'sadness': 0.06,
    'dominant_emotion': 'joy'
}
```

The numbers above are illustrative placeholders, not actual API results.

## Validate the Package

Run the following command from the project root:

```powershell
python -c "from EmotionDetection.emotion_detection import emotion_detector; print(callable(emotion_detector))"
```

Expected output:

```text
True
```

This verifies that the function can be imported and is callable. The actual package structure must match the import path.

## Run the Application

Start the Flask server:

```powershell
python server.py
```

Open the application in your browser:

http://127.0.0.1:5000/

Enter a sentence and submit it to display the emotion scores and dominant emotion.

The live prediction requires the configured Watson NLP endpoint to be reachable.

## Run Unit Tests

Execute:

```powershell
python -m unittest -v test_emotion_detection.py
```

The tests should verify:

- Joy is identified as the dominant emotion for an appropriate input.
- Anger is identified as the dominant emotion for an appropriate input.
- Disgust is identified as the dominant emotion for an appropriate input.
- Sadness is identified as the dominant emotion for an appropriate input.
- Fear is identified as the dominant emotion for an appropriate input.
- The output contains all required keys.
- Invalid inputs and HTTP errors are handled correctly.

Mocked unit tests can run without making live API requests. Report the actual test results rather than assuming every test has passed.

## Error Handling

The application should handle HTTP 400 responses according to the assignment requirements and detect blank or whitespace-only input in the Flask route.

For invalid input, the web interface should display an appropriate message, such as:

```text
Invalid text! Please try again!
```

Verify the message using the running application.

## Static Code Analysis

Run PyLint on the relevant Python files:

```powershell
python -m pylint server.py
python -m pylint emotion_detection.py
python -m pylint test_emotion_detection.py
```

Fix reported issues and rerun the commands.

The assignment requires evidence of the PyLint result. Record the actual score produced by the tool; do not assume a perfect score without running the analysis.

## Screenshots

Save the required screenshots in the `screenshots/` directory.

| Filename | Purpose |
|---|---|
| `6b_deployment_test.png` | Shows the running application with entered text and a completed emotion prediction. |
| `7c_error_handling_interface.png` | Shows the error message displayed for blank input. |

Ensure each screenshot contains the actual application output required by the assignment.

## Assignment Task Mapping

| Task | Description | Relevant files |
|---|---|---|
| 1 | GitHub repository and README | `README.md` |
| 2 | Emotion detection implementation | `emotion_detection.py` |
| 3 | Format the emotion scores and dominant emotion | `emotion_detection.py` |
| 4 | Create and validate the package | `EmotionDetection/__init__.py` and package module |
| 5 | Run unit tests | `test_emotion_detection.py` |
| 6 | Deploy the application using Flask | `server.py`, `templates/index.html`, `static/style.css` |
| 7 | Implement error handling | `emotion_detection.py`, `server.py` |
| 8 | Perform static code analysis | Python source files and PyLint output |

## Repository

**Required IBM Skills Network assignment repository:**

https://github.com/purushottam775/oaqjp-final-project-emb-ai

**Additional project repository, if maintained separately:**

https://github.com/purushottam775/emotion-detector

## License

This project is intended for educational purposes as part of the IBM Skills Network Emotion Detector assignment. Refer to the repository's license file for applicable licensing terms.
