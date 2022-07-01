class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            # If the previous number is not in our set then
            # we are at the start of a sequence
            if (num - 1) not in num_set:
                seq_len = 0

                # For every value, we'll increment by seq_len
                # to see if the following sequence is in the
                # and then increment seq_len by 1 to get
                # the next sequence
                while num + seq_len in num_set:
                    seq_len += 1

                max_length = max(max_length, seq_len)

        return max_length

# Time Complexity: O(n)
# Space Complexity: O(n)