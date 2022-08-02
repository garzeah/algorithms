class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort in-place keep numbers in ascending order
        nums.sort()

        # Counter for valid triplet to make triangle
        valid_triplet = 0

        for i in range(len(nums) - 1, -1, -1):

            third_edge = nums[i] # Want 3rd edge to be the current largest
            index_of_first_edge, index_of_second_edge = 0, i - 1

            # Make triplets using basic triangle property a + b > c
            while index_of_first_edge < index_of_second_edge:
                first_edge = nums[index_of_first_edge]
                second_edge = nums[index_of_second_edge]

                if first_edge + second_edge > third_edge:
                    valid_triplet += (index_of_second_edge - index_of_first_edge)
                    # Second edge large enough make it smaller and try next run
                    index_of_second_edge -= 1
                else:
                    # First edge is too small make it larger and try next run
                    index_of_first_edge += 1

        return valid_triplet

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/valid-triangle-number/discuss/487683/Python-O(-n2-)-sol.-based-on-sliding-window-and-sorting.-85%2B-With-explanation