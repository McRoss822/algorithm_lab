import unittest
from hamster_shop import hamster_farm


class HamsterFarmTest(unittest.TestCase):

    def test_first(self):
        hamsters = [[1, 2], [2, 2], [3, 1]]
        food = 7
        hamster_count = 3
        expected = 2
        self.assertEqual(hamster_farm(hamsters, food, hamster_count), expected, 'incorrect')

    def test_second(self):
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        food = 19
        hamster_count = 4
        expected = 3
        self.assertEqual(hamster_farm(hamsters, food, hamster_count), expected, 'incorrect')

    def test_third(self):
        hamsters = [[1, 50000], [1, 60000]]
        food = 2
        hamster_count = 2
        expected = 1
        self.assertEqual(hamster_farm(hamsters, food, hamster_count), expected, 'incorrect')


if __name__ == "__main__":
    unittest.main()        