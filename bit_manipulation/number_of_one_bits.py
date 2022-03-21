class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            # Counting the amount of 1 remainders
            count += n % 2
            # Shifting the bits to the right to get the next number
            n = n >> 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
