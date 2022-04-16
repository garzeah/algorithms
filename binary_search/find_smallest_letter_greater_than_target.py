class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] > target:
                right = mid - 1
            else: # target < letters[mid]:
                left = mid + 1

        # Since the loop is running until 'left <= right',
        # so at the right of the while loop, 'left == right + 1'
        return letters[left] if left != len(letters) else letters[0]

# Time Complexity: O(logN)
# Space Complexity: O(1)