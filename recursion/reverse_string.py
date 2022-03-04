class Solution:
    def reverseString(self, s: List[str]) -> None:
        return self.helper(0, len(s) - 1, s)

    def helper(self, left, right, s):
        # Base case
        if left >= right:
            return

        # General case
        s[left], s[right] = s[right], s[left]

        self.helper(left + 1, right - 1, s)

# Time Complexity: O(n)
# Space Complexity: O(1)