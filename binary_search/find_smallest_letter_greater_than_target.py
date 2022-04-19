class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if letters[mid] > target:
                end = mid - 1
            else: # target < letters[mid]:
                start = mid + 1


        # Whenever binary search finishes, our start will be in the position
        # it would've been if it were inside the array Since it wraps around,
        # when our start == len(letters), we want to return the 1st value
        return letters[start] if start != len(letters) else letters[0]

# Time Complexity: O(logN)
# Space Complexity: O(1)