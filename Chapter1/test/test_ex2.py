import unittest
import sys
from ex2 import Bits, CompressedGene


class TestBits(unittest.TestCase):

    def setUp(self) -> None:
        self.bits = Bits()
        self.bits.push(0b1).push(0b1).push(0b0).push(0b1)

    def test_getitem(self):
        self.assertEqual(0b1, self.bits[0])
        self.assertEqual(0b1, self.bits[1])
        self.assertEqual(0b0, self.bits[2])
        self.assertEqual(0b1, self.bits[3])

    def test_iterate(self):
        self.assertEqual([1, 1, 0, 1], list(self.bits))

    def test_len(self):
        self.assertEqual(4, len(self.bits))

    def test_append_multibit(self):
        bits = Bits()
        bits.push(0b11, num=2)
        bits.push(0b01, num=2)
        self.assertEqual([1, 1, 0, 1], list(bits))


class TestCompressedGene(unittest.TestCase):

    def setUp(self) -> None:
        self.original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
        self.compressed = CompressedGene(self.original)

    def test_compressed_size(self):
        self.assertEqual(
            2320,
            sys.getsizeof(self.compressed.bit_string())
        )

    def test_original_matches_decompressed(self):
        self.assertEqual(
            self.original,
            self.compressed.decompress()
        )

    def test_small(self):
        self.assertEqual("ACGT", CompressedGene("ACGT").decompress())


if __name__ == '__main__':
    unittest.main()
