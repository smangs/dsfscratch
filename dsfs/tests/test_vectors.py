import unittest

from dsfs import vectors


class TestVectors(unittest.TestCase):
    def test_add_vectors(self):
        """
        Test that it can add vectors
        """
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        result = vectors.add(v1, v2)
        self.assertEqual(result, [5, 7, 9])

    def test_subtract_vectors(self):
        """
        Test that it can subtract vectors
        """
        v1 = [5, 7, 9]
        v2 = [4, 5, 6]
        result = vectors.subtract(v1, v2)
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()