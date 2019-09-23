import unittest
from ex2 import Bits

class TestBits(unittest.TestCase):

    def setUp(self) -> None:
        self.bits = Bits()
        self.bits.append(0b1)
        self.bits.append(0b1)
        self.bits.append(0b0)
        self.bits.append(0b1)

    def test_getitem(self):
        self.assertEqual(0b1, self.bits[0])
        self.assertEqual(0b1, self.bits[1])
        self.assertEqual(0b0, self.bits[2])
        self.assertEqual(0b1, self.bits[3])

    def test_iterate(self):
        self.assertEqual([1,1,0,1], list(self.bits))


if __name__ == '__main__':
    unittest.main()
