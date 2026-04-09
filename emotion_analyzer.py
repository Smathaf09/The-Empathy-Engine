from transformers import pipeline

class EmotionAnalyzer:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )

    def analyze(self, text: str):
        results = self.classifier(text)[0]

        results = sorted(results, key=lambda x: x['score'], reverse=True)
        top = results[0]

        label = top['label']
        confidence = top['score']

        # intensity logic (fix this properly)
        intensity = min(
            confidence + (text.count("!") * 0.05),
            1.0
        )

        return {
            "label": label,
            "confidence": confidence,
            "intensity": intensity
        }