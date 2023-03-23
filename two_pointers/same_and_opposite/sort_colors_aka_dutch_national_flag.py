class Solution:
    def sortColors(self, arr: List[int]) -> None:
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        # Left/right will be used to swap 0/2
        left, right = 0, len(arr) - 1
        i = 0

        while (i <= right):
            # Swap to pos. of left pointer (0)
            if arr[i] == 0:
                swap(left, i);
                left += 1;
                i += 1;
            # After we swap, we don't want to increment i since
            # we may have to swap that value as well
            elif arr[i] == 2:
                swap(right, i)
                right -= 1
            # Increment since we are only swapping 0 and 2
            else:
                i += 1

        return arr;

# Time Complexity: O(n)
# Space Complexity: O(1)