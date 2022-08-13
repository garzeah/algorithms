class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums) # Will be used to check to build a new subsequence
        hm = Counter() # a hypothetical map that will be used to check if we
        # can place a number in an existing sequence

        # We want to checked if split the array into consecutive sequences
        for i in nums:
            if freq[i] == 0: # No nums longer available to process
                continue

            freq[i] -= 1
            # Place number in an existing subsequence if possible
            if hm[i - 1] > 0:
                hm[i - 1] -= 1
                hm[i] += 1
            # Builds a new subsequence of length 3
            elif freq[i + 1] and freq[i + 2]:
                freq[i + 1] -= 1
                freq[i + 2] -= 1
                hm[i + 2] += 1 # Stores number to see if it can be reused
            # Otherwise, we can't place our number, so we return false
            else:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution:
    # 1) https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C++Python-Esay-Understand-Solution/892981
    # 2) https://www.youtube.com/watch?v=uJ8BAQ8lASE