import unittest
from deforestation_main import calculate_square


class MyTestCase(unittest.TestCase):
    def test_correctness(self):
        input = 2
        output = 4
        self.assertEqual(calculate_square(input), output)


if __name__ == '__main__':
    unittest.main()
