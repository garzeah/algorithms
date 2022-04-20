class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.binary_search(arr, x)
        low, high = index - k, index + k

        low = max(low, 0)  # 'low' should not be less than zero
        # 'high' should not be greater the size of the array
        high = min(high, len(arr) - 1)

        minHeap = []

        # add all candidate elements to the min heap, sorted by their absolute difference from 'x'
        for i in range(low, high+1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))

        # we need the top 'k' elements having smallest difference from 'x'
        result = []
        for _ in range(k):
            result.append(heappop(minHeap)[1])

        result.sort()
        return result

    def binary_search(self, arr,  target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if low > 0:
            return low - 1
        return low