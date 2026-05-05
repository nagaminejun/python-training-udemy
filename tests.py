import unittest

class TestDemo(unittest.TestCase):
    def test_example(self):
        print("\n--- テストが実行されました！ ---")
        self.assertEqual(1, 1)
