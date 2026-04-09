from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import os


class TTSEngine:
    def __init__(self, api_key):
        self.client = ElevenLabs(api_key=api_key)

        # Choose a good voice (you can experiment later)
        self.voice_id = "6UkJ4Jo3gctWqKHSD3V8"  # Rachel (default high quality)

    def map_emotion_to_voice(self, emotion, intensity):
        """
        Convert emotion + intensity into ElevenLabs parameters
        """

        stability = 0.5
        similarity_boost = 0.75
        style = 0.0

        if emotion == "joy":
            stability = 0.3 - (intensity * 0.2)
            style = 0.6 + (intensity * 0.4)

        elif emotion == "anger":
            stability = 0.4 - (intensity * 0.2)
            style = 0.7

        elif emotion == "sadness":
            stability = 0.7 + (intensity * 0.2)
            style = 0.2

        elif emotion == "fear":
            stability = 0.6
            style = 0.4 + (intensity * 0.3)

        elif emotion == "surprise":
            stability = 0.2
            style = 0.8

        return VoiceSettings(
            stability=max(0, min(stability, 1)),
            similarity_boost=similarity_boost,
            style=max(0, min(style, 1)),
            use_speaker_boost=True
        )

    def generate_audio(self, text, emotion, intensity, output_path="output.mp3"):

        settings = self.map_emotion_to_voice(emotion, intensity)

        audio_stream = self.client.text_to_speech.convert(
        text=text,
        voice_id=self.voice_id,
        voice_settings=settings
        )

        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                if chunk:
                    f.write(chunk)

        return os.path.abspath(output_path)