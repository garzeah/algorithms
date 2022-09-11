class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Will use a freq counter to build new subsequences and
        # subsequence map that records at which a subsequence
        # ends to see if we can add a new value in
        freq, ends = Counter(nums), Counter()

        for num in nums:
            if freq[num] == 0: # No nums longer available to process
                continue

            freq[num] -= 1
            # Checks if we can place a number in an existing subsequence
            if ends[num - 1] > 0:
                ends[num - 1] -= 1
                ends[num] += 1
            # Builds a new subsequence of length 3
            elif freq[num + 1] and freq[num + 2]:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                ends[num + 2] += 1 # Indicates that we have a subsequence that ends w/ num + 2
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