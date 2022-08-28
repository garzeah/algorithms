class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        res = []
        i = 0

        # For each position in our number, we will convert it
        # to roman numerals. Since we are working backwards
        # we will have to reverse at the end
        while num > 0:
            n = num % 10

            # I to III
            if 1 <= n <= 3:
                res.append(ones[i] * n)

            # IV
            elif n == 4:
                res.append(ones[i] + fives[i])

            # V to VIII
            elif 5 <= n <= 8:
                res.append(fives[i] + (ones[i] * (n - 5)))

            # IX
            elif n == 9:
                res.append(ones[i] + ones[i+1])

            i += 1
            num //= 10

        return "".join(res[::-1])

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/integer-to-roman/discuss/531193/Python-solution-without-big-table