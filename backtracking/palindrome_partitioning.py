class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr_path, res = []
        return self.backtrack(s, res, curr_path, 0)

    def backtrack(self, s, start, curr_path, res):
        # When we reach the last index append the results
        if start >= len(s):
            res.append(list(curr_path))
            return

        # For each substring, we want to check if it is a
        # palindrome then add the remaining letter in and
        # check if it is a palindrome as well
        for end in range(start, len(s)):
            if self.is_palindrome(s[start:end + 1]):
                curr_path.append(s[start:end + 1])
                # We pass in end + 1 instead of start + 1 because
                # we are partitioning the word and want to grab
                # each sequence of it
                self.backtrack(s, end + 1, curr_path, res)
                curr_path.pop()

        return res

    def is_palindrome(self, s):
        start, end = 0, len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

# Time complexity: O(2^n)
# Space complexity: O(2^n)
# Solution: https://www.youtube.com/watch?v=3jvWodd7ht0