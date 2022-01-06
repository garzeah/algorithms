class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        quadruplets = []

        for i in range(len(arr)):
            # Skip same element to avoid duplicate quadruplets
            if i > 0 and arr[i] == arr[i - 1]:
                continue


            for j in range(i + 1, len(arr)):
                # Skip same element to avoid duplicate quadruplets
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                Solution.search_pairs(arr, target, i, j, quadruplets)

        return quadruplets



    def search_pairs(arr, target, i, j, quadruplets):
        left, right = j + 1, len(arr) - 1

        while (left < right):
            quad_sum = arr[i] + arr[j] + arr[left] + arr[right]
            if quad_sum == target:  # Found the quadruplet
                quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                left += 1
                right -= 1
                while (left < right and arr[left] == arr[left - 1]):
                    left += 1  # Skip same element to avoid duplicate quadruplets
                while (left < right and arr[right] == arr[right + 1]):
                    right -= 1  # Skip same element to avoid duplicate quadruplets
            elif quad_sum < target:
                left += 1  # We need a pair with a bigger sum
            else:
                right -= 1  # We need a pair with a smaller sum

# Time Complexity: Sorting the array will take O(N*logN). Overall
# searchQuadruplets() will take O(N * logN + N^3), which is
# asymptotically equivalent to O(N^3).

# Space Complexity: The space complexity of the above algorithm
# will be O(N) which is required for sorting.