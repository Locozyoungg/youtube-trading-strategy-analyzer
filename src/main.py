from downloader import download_audio
from transcriber import transcribe_audio
from analyzer import preprocess_text, extract_strategies

def main():
    # Replace with your YouTube video URL
    video_url = "https://www.youtube.com/watch?v=VIDEO_ID"
    
    # Step 1: Download audio from the video
    audio_path = download_audio(video_url)
    
    # Step 2: Transcribe the audio
    transcription_text = transcribe_audio(audio_path)
    
    # Step 3: Preprocess the transcription
    cleaned_text = preprocess_text(transcription_text)
    print("Cleaned Text:", cleaned_text)
    
    # Step 4: Extract and summarize trading strategies
    strategies = extract_strategies(cleaned_text)
    print("Extracted Trading Strategies:", strategies)

if __name__ == "__main__":
    main()
