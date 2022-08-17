class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # If we have an array of size 1 and it's 1, return true
        if len(target) == sum(target):
            return True

        # If we have an array of size 1, return false
        if len(target) == 1:
            return False

        # Another way to think about this is that we can start from our target
        # sum and in our current array we can find the max num and subtract it
        # with the remaining values in our array and repeatedly do that. If we
        # arrive at [1, 1, 1] then return we can construct a target arr w/
        # multiple sums. For example...
        # [9, 3, 5] 9  : 9 - (3 + 5) = 1
        # [1, 3, 5] 5  : 5 - (3 + 1) = 1
        # [1, 3, 1] 3  : 3 - (1 + 1) = 1
        # [1, 1, 1]

        # [8, 5] 8  : 8 - 5 = 3
        # [3, 5] 5  : 5 - 3 = 2
        # [3, 2] 3  : 3 - 2 = 1
        # [1, 2] 2  : 2 - 1 = 1
        # [1, 1]

        # modulo conditional example
        # [1, 10] 10: 10 - 1 = 9; 9 > 1 (rest) = (9 % 1) + 1 (rest) = 0 + 1
        # [1, 1]

        # [5, 2] 5: 5 - 2 = 3; 3 > 2 (rest) = (3 % 2) + 2 (rest) = 1 + 2 = 3

        # So we can use a max_heap to get the max of of an arr
        max_heap = [-num for num in target]
        total = sum(target)
        heapify(max_heap)

        # If we have a value of -1, that means we've reached our all 1's case
        # meaning we can construct a target array w/ multiple sums
        while max_heap[0] != -1:
            curr_max = -heappop(max_heap) # current max number 10
            rest = total - curr_max # remaining numbers 11 - 10 = 1
            new = curr_max - rest # subtracting max w/ remaining nums 10 - 1 = 9

            # If our new value is less than equal 0 then that means we can't
            # reach the case of hitting all 1's in our target array
            if new <= 0:
                return False

            # If value is greater than the rest of the values, we can
            # perform (new % rest) in cases like [1, 10] will yield a
            # 0 and we can add the rest to it and it will give a 1.
            # We're using rest and not 1 because if we have a
            # remainder and add rest, we can get the orig. val
            if new > rest:
                new = (new % rest) + rest

            # Keep track of the new total
            total -= curr_max
            total += new

            heappush(max_heap, -new)

        return True

# Time Complexity: At least O(n log n) since we're using a heap and storing the
# whole array in it.

# Space Complexity: O(n)

# Solution: https://www.youtube.com/watch?v=azLBGMaw9qI