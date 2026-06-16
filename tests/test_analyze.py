import unittest

from creator_signal_agent.analyze import score_signal


class AnalyzeTests(unittest.TestCase):
    def test_score_signal_prefers_high_momentum_low_saturation(self):
        strong = {"momentum": "0.9", "relevance": "0.9", "saturation": "0.2", "effort": "0.3"}
        weak = {"momentum": "0.4", "relevance": "0.4", "saturation": "0.9", "effort": "0.8"}

        self.assertGreater(score_signal(strong), score_signal(weak))


if __name__ == "__main__":
    unittest.main()
