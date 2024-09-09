import unittest
from src.downloader import download_audio
import os

class TestDownloader(unittest.TestCase):
    def test_download_audio(self):
        video_url = "https://www.youtube.com/watch?v=YOUR_TEST_VIDEO_ID"
        audio_path = download_audio(video_url, output_path='test_downloads')
        self.assertTrue(os.path.exists(audio_path))
        os.remove(audio_path)  # Clean up

if __name__ == '__main__':
    unittest.main()
