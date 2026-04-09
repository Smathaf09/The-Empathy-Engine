class VoiceMapper:

    PROFILES = {
        "joy": {"rate": (200, 260), "volume": (0.8, 1.0)},
        "anger": {"rate": (170, 210), "volume": (0.8, 1.0)},
        "sadness": {"rate": (120, 160), "volume": (0.4, 0.7)},
        "fear": {"rate": (150, 190), "volume": (0.5, 0.8)},
        "surprise": {"rate": (220, 280), "volume": (0.9, 1.0)},
        "neutral": {"rate": (180, 200), "volume": (0.6, 0.8)}
    }

    def scale(self, min_val, max_val, intensity):
        return min_val + (max_val - min_val) * intensity

    def get_parameters(self, emotion_label: str, intensity: float):
        profile = self.PROFILES.get(emotion_label, self.PROFILES["neutral"])

        return {
            "rate": int(self.scale(*profile["rate"], intensity)),
            "volume": round(self.scale(*profile["volume"], intensity), 2)
        }