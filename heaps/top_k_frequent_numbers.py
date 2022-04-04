class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map, min_heap, output = {}, [], []

        # Find the frequency of each number
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Go through all numbers of the freq_map and push them in
        # the min_heap, which will have top k frequent numbers.
        # If the heap size is more than k, we remove the smallest (top) number
        for (num, frequency) in freq_map.items():
            heappush(min_heap, [frequency, num])

            if len(min_heap) > k:
                heappop(min_heap)

        for (freq, num) in min_heap:
            output.append(num)

        return output

# Time Complexity: O(N + N*logK)
# Space Complexity: O(N) bc we store every value in our map