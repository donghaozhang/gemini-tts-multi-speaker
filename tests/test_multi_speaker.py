import os
import unittest

from gemini_tts_example import text_to_speech_multi_speaker


class MultiSpeakerTestCase(unittest.TestCase):
    def test_too_many_speakers(self):
        with self.assertRaises(ValueError) as cm:
            text_to_speech_multi_speaker(
                "A: hi\nB: hello\nC: hey",
                [
                    {"name": "A", "voice": "kore"},
                    {"name": "B", "voice": "puck"},
                    {"name": "C", "voice": "leda"},
                ],
            )
        self.assertIn("maximum 2 speakers", str(cm.exception))

    def test_too_few_speakers(self):
        with self.assertRaises(ValueError) as cm:
            text_to_speech_multi_speaker(
                "A: hi",
                [{"name": "A", "voice": "kore"}],
            )
        self.assertIn("at least 2 speakers", str(cm.exception))

    def test_missing_api_key(self):
        prev = os.environ.pop("GEMINI_API_KEY", None)
        try:
            with self.assertRaises(ValueError) as cm:
                text_to_speech_multi_speaker(
                    "A: hi\nB: hello",
                    [
                        {"name": "A", "voice": "kore"},
                        {"name": "B", "voice": "puck"},
                    ],
                )
            self.assertIn("GEMINI_API_KEY", str(cm.exception))
        finally:
            if prev is not None:
                os.environ["GEMINI_API_KEY"] = prev


if __name__ == "__main__":
    unittest.main()
