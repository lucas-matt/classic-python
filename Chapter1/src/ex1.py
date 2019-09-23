from functools import lru_cache

# Write yet another function that solves for element n of the Fibonacci sequence,
# using a technique of your own design. Write unit tests that evaluate its correctness and performance
# relative to the other versions in this chapter.

@lru_cache()
def fib(n: int) -> int:
    return fib(n-1) + fib(n-2) if n >= 2 else n