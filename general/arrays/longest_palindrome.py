class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        has_odd = False
        res = 0

        for key in freq:
            # If even, add all the frequencies
            if freq[key] % 2 == 0:
                res += freq[key]

            # If odd, want to add every even to
            # make the longest palindrome
            else:
                res += freq[key] - 1
                odd = True

        # If our freq contains an odd, we can use
        # up one of the remaining odds to make a
        # valid palindrome
        if has_odd:
            res += 1

        return res

# Time Complexity: O(n)

# Space Complexity: O(26) since we are only storing the
# values of alphabetical characters