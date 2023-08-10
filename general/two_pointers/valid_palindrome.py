class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            # Sliding left is not alphanumeric
            while left < right and s[left].isalnum() is False:
                left += 1

            # Sliding right is not alphanumeric
            while left < right and s[right].isalnum() is False:
                right -= 1

            # Not a palindrome
            if s[left] != s[right]:
                return False

            # Checking next letter
            left += 1
            right -= 1

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)


