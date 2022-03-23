class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Get the XOR of the all the numbers
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num

        # Get the rightmost bit that is '1'
        rightmost_set_bit = 1
        while (rightmost_set_bit & n1xn2) == 0:
            rightmost_set_bit = rightmost_set_bit << 1
        num1, num2 = 0, 0

        for num in nums:
            if (num & rightmost_set_bit) != 0:  # The bit is set
                num1 ^= num
            else:  # The bit is not set
                num2 ^= num

        return [num1, num2]

# Time Complexity: O(n)
# Space Complexity: O(1)