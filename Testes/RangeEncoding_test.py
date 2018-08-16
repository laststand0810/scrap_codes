import unittest
import source.RangeEncoding as RE

class TestRangeCoding(unittest.TestCase):

    def test_minRanges(self):
        encode = RE.RangeEncoding()
        self.assertEqual(encode.minRanges([1,2,3,4,5]),1)
        self.assertEqual(encode.minRanges([1,]), 1)
        emptyRange = []
        self.assertEqual(encode.minRanges(emptyRange), 0)
        self.assertEqual(encode.minRanges([1, 2, 4, 5]), 2)

if __name__ == "__main__":
    unittest.main()