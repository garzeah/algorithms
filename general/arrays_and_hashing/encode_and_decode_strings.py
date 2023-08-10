class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        # We want to find the length of the word and set
        # a delimiter in this format 5#Hello5#World
        for word in strs:
            res += str(len(word)) + '#' + word

        return res


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0

        while i < len(s):
            j = i # This will point at the length

            # Want to get the length of the word
            while s[j] != '#':
                j += 1

            # When we have the length we can get the word by
            # starting at s[j + 1 : j + 1 + length]
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length # Move up pointer to next word

        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# TC/SC: O(n)
# Solution: https://www.youtube.com/watch?v=B1k_sxOSgv8