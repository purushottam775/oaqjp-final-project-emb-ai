# Submission Checklist — IBM Emotion Detector Final Project

> Maps each of the 16 grading points to the actual evidence file or terminal command.

---

## Grading Evidence Map

| # | Grading Point | Evidence | Location / Command |
|---|--------------|----------|-------------------|
| 1 | Public GitHub README URL | README.md in public repo | https://github.com/purushottam775/emotion-detector/blob/main/README.md |
| 2 | `emotion_detection.py` implementation | Source file | [`emotion_detection.py`](emotion_detection.py) |
| 3 | Import and execution terminal output | Run command | `python -c "from EmotionDetection import emotion_detector; print(callable(emotion_detector))"` |
| 4 | Correct output-format implementation | Source file | [`emotion_detection.py`](emotion_detection.py) — `_parse_response()` returns the 6-key dict |
| 5 | Output-format terminal output | Run command | `python -c "from EmotionDetection import emotion_detector; import json; print(json.dumps(emotion_detector('I love this!'), indent=2))"` |
| 6 | Public GitHub URL for `EmotionDetection/__init__.py` | Source file in repo | https://github.com/purushottam775/emotion-detector/blob/main/EmotionDetection/__init__.py |
| 7 | Package validation terminal output | Run command | `python -c "from EmotionDetection import emotion_detector; print('callable:', callable(emotion_detector))"` |
| 8 | Unit test source code | Source file | [`test_emotion_detection.py`](test_emotion_detection.py) |
| 9 | Passing unit test output | Run command | `python -m unittest -v test_emotion_detection.py` → **Ran 15 tests in ~0.004s — OK** |
| 10 | `server.py` Flask implementation | Source file | [`server.py`](server.py) |
| 11 | `6b_deployment_test.png` | Screenshot | [`screenshots/6b_deployment_test.png`](screenshots/6b_deployment_test.png) |
| 12 | HTTP 400 handling implementation | Source file | [`emotion_detection.py`](emotion_detection.py) — `if response.status_code == 400: return dict(_NONE_RESULT)` |
| 13 | Blank-input handling in `server.py` | Source file | [`server.py`](server.py) — `if not text_to_analyze: return jsonify({"error": "Invalid text! Please try again!"}), 400` |
| 14 | `7c_error_handling_interface.png` | Screenshot | [`screenshots/7c_error_handling_interface.png`](screenshots/7c_error_handling_interface.png) |
| 15 | Static-analysis implementation and command | Command | `python -m pylint server.py` |
| 16 | Terminal output showing final PyLint score | Actual output | `Your code has been rated at 10.00/10` |

---

## Verified Terminal Outputs

### Package Import Validation (Item 3 & 7)
```
$ python -c "from EmotionDetection import emotion_detector; print('callable:', callable(emotion_detector))"
callable: True
```

### Unit Test Results (Item 9)
```
$ python -m unittest -v test_emotion_detection.py

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

### PyLint Score — server.py (Items 15 & 16)
```
$ python -m pylint server.py

------------------------------------
Your code has been rated at 10.00/10
```

### PyLint Score — emotion_detection.py
```
$ python -m pylint emotion_detection.py

------------------------------------
Your code has been rated at 10.00/10
```

### PyLint Score — test_emotion_detection.py
```
$ python -m pylint test_emotion_detection.py

------------------------------------
Your code has been rated at 10.00/10
```

### Flask Blank-Input Error Handling (Item 13)
```
$ python -c "
from server import app; import json
c = app.test_client()
r = c.get('/emotionDetector?textToAnalyze=')
print(r.status_code, json.loads(r.data))
"
400 {'error': 'Invalid text! Please try again!'}
```

---

## Screenshot Instructions

> The two required screenshots must be captured manually by running the Flask server locally:

### 6b — Deployment Test Screenshot
1. Run: `python server.py`
2. Open: http://127.0.0.1:5000/
3. Enter: `"I am so happy today!"` and click **Analyse Emotion**
4. Capture the browser window showing the emotion scores
5. Save as: `screenshots/6b_deployment_test.png`

### 7c — Error Handling Screenshot
1. Run: `python server.py`
2. Open: http://127.0.0.1:5000/
3. Click **Analyse Emotion** without entering any text (or enter only spaces)
4. Capture the browser showing: **"Invalid text! Please try again!"**
5. Save as: `screenshots/7c_error_handling_interface.png`

---

## Repository Status

| Item | Status |
|------|--------|
| GitHub repository | https://github.com/purushottam775/emotion-detector |
| All source files created | ✅ |
| Unit tests: 15/15 passing | ✅ |
| PyLint 10.00/10 on all files | ✅ |
| Flask app validated with test client | ✅ |
| Screenshots | ⚠️ Requires manual capture (see above) |
| Git push to GitHub | ⚠️ Requires your Git credentials |

---

## Manual Steps Remaining

1. **Push to GitHub** — Run these commands in the project directory:
   ```powershell
   cd "D:\New folder (15)\New folder\emotion-detector"
   git add .
   git commit -m "Complete all 8 assignment tasks"
   git push origin main
   ```
   You will be prompted for your GitHub username and Personal Access Token (PAT).

2. **Capture screenshots** — Start `python server.py`, open the browser, and save the two screenshots per the instructions above.

