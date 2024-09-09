from google.cloud import speech

def transcribe_audio(audio_file_path):
    """
    Transcribes audio from a file using Google Cloud Speech-to-Text.
    
    Args:
        audio_file_path (str): Path to the audio file.
    
    Returns:
        str: Transcribed text.
    """
    client = speech.SpeechClient()
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_automatic_punctuation=True
    )
    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript + " "
    return transcription
