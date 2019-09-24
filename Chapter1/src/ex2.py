from __future__ import annotations
from typing import Iterable, Iterator

# You saw how the simple int type in Python can be used to represent a bit string.
# Write an ergonomic wrapper around int that can be used generically as a
# sequence of bits (make it iterable and implement __getitem__()). Reimplement CompressedGene, using the wrapper


class Bits(Iterable[bool]):

    def __init__(self) -> None:
        self.bit_string = 1

    def push(self, val: int, num=1) -> Bits:
        self.bit_string <<= num
        self.bit_string |= val
        return self

    def __iter__(self) -> Iterator[int]:
        for i in reversed(range(0, self.bit_string.bit_length() - 1)):
            yield self.bit_string >> i & 0b1

    def __getitem__(self, item) -> int:
        return self.bit_string >> (self.bit_string.bit_length() - item - 2) & 0b1

    def __len__(self):
        return self.bit_string.bit_length() - 1


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bits = Bits()  # start with sentinel
        for nucleotide in gene.upper():
            if nucleotide == "A":  # change last two bits to 00
                self.bits.push(0b00, num=2)
            elif nucleotide == "C":  # change last two bits to 01
                self.bits.push(0b01, num=2)
            elif nucleotide == "G":  # change last two bits to 10
                self.bits.push(0b10, num=2)
            elif nucleotide == "T":  # change last two bits to 11
                self.bits.push(0b11, num=2)
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        pairs = [(self.bits[2*i], self.bits[2*i+1]) for i in range(0, int(len(self.bits)/2))]
        for x, y in pairs:  # - 1 to exclude sentinel
            if (x, y) == (0, 0):  # A
                gene += "A"
            elif (x, y) == (0, 1):  # C
                gene += "C"
            elif (x, y) == (1, 0):  # G
                gene += "G"
            elif (x, y) == (1, 1):  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(self.bits))
        return gene  # [::-1] reverses string by slicing backwards

    def bit_string(self) -> int:
        return self.bits.bit_string

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()
