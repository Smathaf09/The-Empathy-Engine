#  Empathy Engine: Giving AI a Human Voice

##  Overview

The **Empathy Engine** is an AI-powered system that transforms plain text into emotionally expressive speech. Unlike traditional Text-to-Speech (TTS) systems that produce robotic and monotonic output, this project dynamically adapts voice characteristics based on the detected emotion of the input text.

The goal is to bridge the gap between **text understanding and human-like voice delivery**, enabling more natural and engaging AI interactions—especially in domains like customer support, sales, and virtual assistants.

---

##  Key Features

### 1. Emotion Detection (Transformer-Based)

* Uses a pre-trained model from **Hugging Face Transformers**
* Detects granular emotions such as:

  * Joy
  * Anger
  * Sadness
  * Fear
  * Surprise
  * Neutral
* Outputs both:

  * Emotion label
  * Intensity score

---

### 2. Emotion-to-Voice Mapping

* Converts emotion + intensity into voice modulation parameters
* Uses:

  * Stability (controls calmness vs expressiveness)
  * Style (controls emotional exaggeration)
  * Similarity boost (voice consistency)

---

### 3. Dynamic Speech Generation (ElevenLabs API)

* Uses high-quality neural voices from ElevenLabs
* Generates realistic, human-like audio output
* Supports expressive tone variation

---

### 4. Intensity Scaling

* Emotion strength directly affects voice output
* Example:

  * *"This is good"* → mild expression
  * *"This is AMAZING!!!"* → strong expressive tone

---

##  System Architecture

```
Input Text
    ↓
Emotion Analyzer (Transformers)
    ↓
Emotion + Intensity
    ↓
Voice Mapper
    ↓
Voice Parameters (stability, style, etc.)
    ↓
ElevenLabs TTS Engine
    ↓
Audio Output (.mp3)
```

---

##  Tech Stack

* **Python 3.12**
* **Hugging Face Transformers**
* **ElevenLabs API**
* **PyTorch**
* **[Can be added later for sentence-level processing in the future] NLTK**

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Smathaf09@/empathy-engine.git
cd empathy-engine
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
"create requirement.txt where you write only :
transformers
torch
huggingface-hub
elevenlabs
nltk"


---

### 3. Setup API Keys

#### ElevenLabs

1. Go to https://elevenlabs.io
2. Generate API key
3. Create a custom voice (required for free tier) - I used my custom one voiceId:6UkJ4Jo3gctWqKHSD3V8

Update in code:

```python
tts = TTSEngine(api_key="YOUR_API_KEY")
```

---

### 4. Run the Project

```bash
python main.py
```

---

##  Usage

```
Console :
Enter text to synthesize (or 'q' to quit): if it works then it will be amazing
Detected Emotion: surprise (Intensity: 0.70)
Applying Voice Params:{'rate': 262, 'volume': 0.97}
SUCCESS: Audio saved

Enter text to synthesize (or 'q' to quit): it will be inappropriate to judge anyone based on looks
Detected Emotion: anger (Intensity: 0.68)
Applying Voice Params:{'rate': 197, 'volume': 0.94}
SUCCESS: Audio saved 

Output:
output.mp3

```

---

##  Important Notes

* Free-tier ElevenLabs users **must use a custom voice**
* Library voices require a paid plan
* First run downloads the transformer model (~300MB)

---

## 📊 Example Behavior

| Input Text               | Detected Emotion | Output Style        |
| ------------------------ | ---------------- | ------------------- |
| "I am so happy!"         | Joy              | Fast, expressive    |
| "This is frustrating..." | Anger            | Controlled, intense |
| "I'm feeling low today"  | Sadness          | Slow, soft          |

Other emotions used : "fear", "surprise", "neutral"
we can add much more....

---

## Future Improvements

* Sentence-level emotion detection
* Multi-emotion audio stitching
* Real-time streaming voice synthesis
* Web interface (FastAPI + frontend)
* SSML-based fine control (using google cloud possibly)

---

##  Challenges Solved

* Bridging text sentiment to voice modulation
* Handling API limitations (free vs paid tiers)
* Designing emotion-intensity scaling logic
* Improving realism beyond traditional TTS

---

##  Conclusion

This project demonstrates how combining **NLP + voice synthesis** can significantly improve human-AI interaction. By adding emotional intelligence to speech, AI systems become more engaging, trustworthy, and effective.

---

## 👨‍💻 Author

**Shaf**

---

## ⭐ If you found this interesting, consider giving it a star!
