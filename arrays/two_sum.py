class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # val : index

        for i, num in enumerate(nums):
            curr_diff = target - num

            # If we see the value again, we have found the two sum
            if curr_diff in prev_map:
                return [prev_map[curr_diff], i]

            # Recording the value and index
            prev_map[num] = i

        return # Not really necessary since we're guaranteed a sol.

# Time Complexity: O(n)
# Space Complexity: O(n)
