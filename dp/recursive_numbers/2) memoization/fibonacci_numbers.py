class Solution:
    def fib(self, n: int) -> int:
        cache = [-1 for x in range(n + 1)]
        return self.helper(n, cache)

    def helper(self, n, cache):
        if n <= 0:
            cache[n] = 0
            return cache[n]

        if n == 1:
            cache[n] = 1
            return cache[n]

        if cache[n] == -1:
            cache[n] = self.helper(n - 2, cache) + self.helper(n - 1, cache)

        return cache[n]