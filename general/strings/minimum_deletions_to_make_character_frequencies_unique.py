class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        unique = set() # Keep track of unique frequencies
        count = 0

        for (char, freq) in freq.items():
            # While we have a frequency and it is in unique, we
            # either want to completely delete it or find a new
            # unique frequency and keep track of the count
            while freq > 0 and freq in unique:
                freq -= 1
                count += 1

            unique.add(freq)

        return count

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/1223602/Python-Easy-Sol-with-Explanation