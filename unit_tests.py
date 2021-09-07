import unittest
from converter import Converter

class TestTimestampGenerator(unittest.TestCase):
    def setUp(self):
        self.sut = Converter()

    def test_timestamps_returns_a_list(self):
        self.assertIsInstance(float, float)

if __name__ == "__main__":
    unittest.main()
