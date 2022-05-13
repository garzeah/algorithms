class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if letters[mid] > target:
                end = mid - 1
            else: # target <= letters[mid]:
                start = mid + 1

        # Whenever binary search finishes, our start will always be
        # ahead of end and we can use that to determine the next
        # value in the array. Since we want to wrap around, if
        # we exceed past the length of letters, we want to
        # return the first value in the array.
        return letters[start] if start != len(letters) else letters[0]

# Time Complexity: O(logN)
# Space Complexity: O(1)