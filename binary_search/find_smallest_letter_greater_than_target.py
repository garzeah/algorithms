class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if letters[mid] > target:
                end = mid - 1
            else: # target < letters[mid]:
                start = mid + 1

        # Since the loop is running until 'start <= end',
        # so at the end of the while loop, 'start == end + 1'
        return letters[start] if left != len(letters) else letters[0]

# Time Complexity: O(logN)
# Space Complexity: O(1)