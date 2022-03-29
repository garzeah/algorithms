class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        # Add the numbers in the min heap
        for num in nums:
            # Add the new number in the min heap
            heappush(min_heap, num)

            # If heap has more than 'k' numbers, remove one number.
            # We are going to keep the kth biggest numbers and since
            # we are using a min_heap the kth largest element will
            # always be at the root of our heap
            if len(min_heap) > k:
                heappop(min_heap)


        # Return the Kth largest number
        return min_heap[0]

# Time Complexity: O(log k) since we are inserting the into our heap
# Space Complexity: O(k) since we are only storing at most k numbers.