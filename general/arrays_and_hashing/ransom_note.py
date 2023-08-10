class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)

        for char in magazine:
            if ransom_count[char]:
                ransom_count[char] -= 1

        for key, val in ransom_count.items():
            if val > 0:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)