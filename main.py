import os
from emotion_analyzer import EmotionAnalyzer
from voice_mapper import VoiceMapper
from tts_engine import TTSEngine



def main():
    print("--- Empathy Engine System Initialized ---")
    
    # Initialize components
    analyzer = EmotionAnalyzer()
    mapper = VoiceMapper()
    # tts = TTSEngine()

    while True:
        user_input = input("\nEnter text to synthesize (or 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            break
        
        if not user_input:
            continue

        # 1. Analyze Emotion
        analysis = analyzer.analyze(user_input)
        label = analysis['label']
        intensity = analysis['intensity']
        
        print(f"Detected Emotion: {label} (Intensity: {intensity:.2f})")

        # 2. Map to Voice Parameters
        params = mapper.get_parameters(label, intensity)
        print(f"Applying Voice Params:{params}")

        # 3. Generate Speech
        # output_file = "output_speech.wav"
        try:
            tts = TTSEngine(api_key="########__API__KEY__#######")

            full_path = tts.generate_audio(     
                text=user_input,
                emotion=label,
                intensity=intensity,
                output_path="output.mp3"
            )
            print(f"SUCCESS: Audio saved to {full_path}")
        except Exception as e:
            print(f"ERROR: Failed to generate audio. {e}")

if __name__ == "__main__":
    main()
