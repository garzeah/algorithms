class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Will use a freq counter to build new subsequences and
        # subsequence map that records at which a subsequence
        # ends to see if we can add a new value in
        freq, ends = Counter(nums), Counter()

        for i in nums:
            if freq[i] == 0: # No nums longer available to process
                continue

            freq[i] -= 1
            # Checks if we can place a number in an existing subsequence
            if ends[i - 1] > 0:
                ends[i - 1] -= 1
                ends[i] += 1
            # Builds a new subsequence of length 3
            elif freq[i + 1] and freq[i + 2]:
                freq[i + 1] -= 1
                freq[i + 2] -= 1
                ends[i + 2] += 1 # Indicates that we have a subsequence that ends w/ i + 2
            # Otherwise, we can't place our number, so we return false
            else:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution:
    # 1) https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C++Python-Esay-Understand-Solution/892981
    # 2) https://www.youtube.com/watch?v=uJ8BAQ8lASE
    # 3) https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/1806697/Python-Solution-with-explanation