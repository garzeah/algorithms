class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        return self.dfs(s, output, [], 0)

    def dfs(self, s, output, curr_path, start):
        # When we reach the last index append the results
        if start >= len(s):
            output.append(list(curr_path))
            return

        # For each substring, we want to check if it is a
        # palindrome then add the remaining letter in and
        # check if it is a palindrome as well
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                curr_path.append(s[start:end+1])
                self.dfs(s, output, curr_path, end + 1)
                curr_path.pop()

        return output

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False

            start, end = start + 1, end - 1

        return True

# Time complexity: O(2^n)
# Space complexity: O(2^n)
# Solution: https://www.youtube.com/watch?v=3jvWodd7ht0