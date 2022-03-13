import unittest
from deforestation_main import calculate_square


class MyTestCase(unittest.TestCase):
    input = 2
    output = 4

    def test_correctness(self):
        self.assertEqual(calculate_square(self.input), self.output)

    def test_type(self):
        self.assertIsInstance(calculate_square(self.input), int)


if __name__ == '__main__':
    unittest.main()
