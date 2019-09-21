import unittest
from ex1 import fib

class MyTestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(12586269025, fib(50))

if __name__ == '__main__':
    unittest.main()
