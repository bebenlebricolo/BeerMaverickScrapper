import unittest
from ..parallel import spread_load_for_parallel

class TestBaseScraper(unittest.TestCase):
    def test_load_spreading(self):
        input_list = [
            "something",
            "something",
            "something",
            "something",
            "something",
            "something",
            "something",
            "something"
        ]

        matrix = spread_load_for_parallel(input_list, 3)
        self.assertEqual(len(matrix), 3)
        self.assertEqual(len(matrix[0]), 3)
        self.assertEqual(len(matrix[1]), 3)
        self.assertEqual(len(matrix[2]), 2)


if __name__ == "__main__" :
    unittest.main()