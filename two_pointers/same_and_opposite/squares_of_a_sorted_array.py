class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        highest_square_idx = len(nums) - 1
        squares = [None] * len(nums)

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            # Since it's sorted, we can use highest_square_idx
            # to place at the end to get our intended order
            if left_square > right_square:
                squares[highest_square_idx] = left_square
                left += 1
            else:
                squares[highest_square_idx] = right_square
                right -= 1

            highest_square_idx -= 1

        return squares

# Time Complexity: O(n) since we iterate it once only

# Space Complexity: O(n) this space is used up in the output array