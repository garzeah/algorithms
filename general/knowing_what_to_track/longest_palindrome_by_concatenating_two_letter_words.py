class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Create Hashmap to maintain count of words
        lookup = Counter(words)
        has_odd, res = False, 0

        # Iterating over the hashmap keys
        for word in lookup.keys():

            # If word is like 'aa', 'bb' then follow this steps
            if word[0] == word[1]:

                # Even Scenario
                # Suppose if count of 'aa' is 2 then we will take all the 4 words
                # As 'aa' + 'aa' is palindrome
                if lookup[word] % 2 == 0:
                    res += lookup[word] * 2
                # Odd Scenario
                # Suppose if count of 'aa' is 3 then we will take all the even words
                # and add the odd one in the end since we can only have 1 odd for
                # it to still be considered a palindrome
                else:
                    res += (lookup[word] - 1) * 2
                    has_odd = True

            # If reverse of word is present in hashmap
            # then we can create palindrome using current and reverse word
            elif word[::-1] in lookup:
                res += min(lookup[word], lookup[word[::-1]]) * 2

        # Since we have an odd, add the remaining odd value
        if has_odd:
            return res + 2

        return res

# TC: O(n)
# SC: https://www.python-techs.com/2022/11/longest-palindrome-by-concatenating.html
