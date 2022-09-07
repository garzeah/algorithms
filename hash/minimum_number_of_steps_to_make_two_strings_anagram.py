class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = Counter(s) # Getting the frequency

        # We can take the frequency and iterate through the other string and try
        # to make the frequencies match as much as possible. If they overlap,
        # we will decrement it otherwise if it doesn't exist or it equals 0
        # then we have to take a step to make an anagram
        res = 0
        for char in t:
            # We have exhausted every possible character in our freq and
            # we still need to make deletions to make an anagram or it
            # doesn't exist and we need to delete that
            if freq[char] <= 0 or char not in freq:
                res += 1
            else:
                freq[char] -= 1

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/discuss/902179/Python-easy-solution-with-explanation-o(n)-time-and-space%3A-faster-97