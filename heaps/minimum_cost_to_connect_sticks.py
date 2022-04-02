class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = []
        result = 0

        # Add all sticks to the min heap
        for stick in sticks:
            heappush(min_heap, stick)

        # Go through the values of the heap, in each step take
        # top (lowest) rope lengths from the min heap connect
        # them and push the result back to the min heap. keep
        # doing this until the heap is left with only one rope
        while len(min_heap) > 1:
            temp = heappop(min_heap) + heappop(min_heap)
            result += temp
            heappush(min_heap, temp)

        return result

# Time Complexity: Given ‘N’ ropes, we need O(N*logN) to insert
# all the ropes in the heap. In each step, while processing the
# heap, we take out two elements from the heap and insert one.
# This means we will have a total of ‘N’ steps, having a total
# time complexity of O(N*logN)

# Space Complexity: O(n)