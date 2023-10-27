import unittest
from labodyn import zigzag_traversal


class MatrixTraverseTest(unittest.TestCase):
    def test_first(self):
        matrix = [
            [1, 2, 5, 6],
            [3, 4, 7, 8],
        ]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(zigzag_traversal(matrix), expected_result, 'incorect')

    def test_second(self):
        matrix = [
            [1, 2, 6, 7, 15],
            [3, 5, 8, 14, 16],
            [4, 9, 13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25]
        ]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                           12, 13, 14, 15, 16, 17, 18, 19,
                           20, 21, 22, 23, 24, 25]
        self.assertEqual(zigzag_traversal(matrix), expected_result, 'incorect')

    def test_3(self):
        matrix = [
            [1, 2, 5, 6],
            [3, 4, 7, 8]
        ]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(zigzag_traversal(matrix), expected_result, 'incorect')

    def test_4(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag_traversal(matrix), expected_result, 'incorect')

    def test_5(self):
        matrix = [[1]]
        expected_result = [1]
        self.assertEqual(zigzag_traversal(matrix), expected_result, 'incorect')

if __name__ == "__main__":
    unittest.main()
