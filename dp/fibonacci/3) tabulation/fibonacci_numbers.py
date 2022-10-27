class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1

        cache = [-1 for x in range(n + 1)]
        first = 0
        second = 1

        for i in range(2, n + 1):
            cache[i] = first + second
            first = second
            second = cache[i]

        return cache[n]