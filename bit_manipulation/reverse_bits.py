class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # Range is 32 bc we have 32 bits
        for i in range(32):
            # 0 & 1 = 0
            # 1 & 1 = 1
            # Trying to get the bit we need from the end so we
            # can add it to the beginning of our result
            bit = (n >> i) & 1

            # 0 | 0 = 0
            # 0 | 1 = 1
            # Want to shift it so we can keep the values before
            res = res | (bit << (31 - i))

        return res

# Time Complexity: O(1)
# Space Complexity: O(1)