class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if num == 0:
            return 1

        # Count number of total bits in 'num'
        bit_count, n = 0, num
        while n > 0:
            bit_count += 1
            n = n >> 1

        # For a number which is a complete power of '2' i.e., it can be written as pow(2, n), if we
        # subtract '1' from such a number, we get a number which has 'n' least significant bits set to '1'.
        # For example, '4' which is a complete power of '2', and '3' (which is one less than 4) has a binary
        # representation of '11' i.e., it has '2' least significant bits set to '1'
        all_bits_set = pow(2, bit_count) - 1

        # From the solution description: complement = number ^ all_bits_set
        return num ^ all_bits_set

# Time Complexity: Time complexity of this solution is O(b)
# where ‘b’ is the number of bits required to store the given number.

# Space Complexity: O(1)