import unittest

from pyforge import chunks, clamp, flatten


class CoreTests(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(12, 0, 10), 10)

    def test_chunks(self):
        self.assertEqual(list(chunks([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]])

    def test_flatten(self):
        self.assertEqual(flatten([[1, 2], [], [3]]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
