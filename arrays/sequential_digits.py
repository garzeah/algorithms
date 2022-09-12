class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        res = []

        for i in range(len(s)):
            for j in range(i + 1,len(s)):
                curr = int(s[i:j + 1])

                if (curr >= low and curr <= high):
                    res.append(curr)

        return sorted(res)

# Time Complexity: O(1) bc only a fixed amount of sequential numbers
# Space Complexity: O(1) bc only a fixed amount of sequential numbers
# Solution: https://leetcode.com/problems/sequential-digits/discuss/853558/Python-Super_Super-easy-Simplest-question-100-faster