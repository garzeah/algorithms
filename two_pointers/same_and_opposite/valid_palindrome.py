class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            # Sliding left is not alphanumeric
            if not s[left].isalnum() is False:
                left += 1
                continue

            # Sliding right is not alphanumeric
            if s[right].isalnum() is False:
                right -= 1
                continue

            # Not a palindrome
            if s[left] != s[right]:
                return False

            # Checking next letter
            if s[left] == s[right]:
                left += 1
                right -= 1

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)


