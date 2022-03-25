class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)

        for num in nums:
            # Check if it's the start of a sequence since no left neighbor
            if (num - 1) not in num_set:
                seq_len = 0
                # As long as we have a right neighbor, we have a sequence
                while (num + seq_len) in num_set:
                    seq_len += 1

                max_length = max(max_length, seq_len)

        return max_length

# Time Complexity: O(n)
# Space Complexity: O(n)