# The testing framework
import unittest

# Tools that make testing easier
import parameterized
import hypothesis
from hypothesis import strategies as hs

# Import the functions you want to test from the contracts
from src.util import fib
from src.contract_spending import plus_one




class TestMath(unittest.TestCase):

    def test_plus_one_fib(self):
        # A simple test
        self.assertEqual(plus_one(1), fib(4))

    @parameterized.parameterized.expand([
        (0, 0),
        (7, 13),
        (11, 89)
    ])
    def test_fib(self, input, output):
        # A simple parameterized test
        self.assertEqual(output, fib(input))

    @hypothesis.given(hs.integers(min_value=0))
    def test_plus_one(self, input):
        # A simple property based test
        self.assertTrue(plus_one(input) > input)


if __name__ == '__main__':
    unittest.main()