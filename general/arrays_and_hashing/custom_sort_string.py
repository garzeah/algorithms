class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = ""

        for char in order:
            while freq[char]:
                res += char
                freq[char] -= 1

        for char in s:
            if freq[char]:
                res += char
                freq[char] -= 1

        return res