class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        # Since we are removing adjacent characters,
        # we can use a stack to keep track of the
        # last character. We can add in the an
        # array of our current char and freq
        # to keep track of when to remove
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        res = ""
        for (char, freq) in stack:
            while freq:
                res += char
                freq -= 1

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)