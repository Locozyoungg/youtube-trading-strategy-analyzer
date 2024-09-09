import unittest
from src.transcriber import transcribe_audio

class TestTranscriber(unittest.TestCase):
    def test_transcribe_audio(self):
        # You would need a test audio file here
        audio_file_path = 'path/to/test_audio.wav'
        transcription = transcribe_audio(audio_file_path)
        self.assertTrue(len(transcription) > 0)

if __name__ == '__main__':
    unittest.main()
