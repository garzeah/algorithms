class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # Store the length of every possible array if subsequent values
        len_heap = [[nums[0], 1]] # [curr, length of subsequence]

        for i in range(1, len(nums)):
            # While we have values in our heap and if we reach the end of a
            # subsequence, if the length is less than 3 then return false
            # since the length needs to be at least 3 or greater. We are
            # comparing it to nums[i] - 1 because we want to check for
            # every 3 values if we have a valid subsequence, we can
            # remove it since it passes, if not return false
            while len(len_heap) > 0 and len_heap[0][0] < nums[i] - 1:
                if len_heap[0][1] < 3:
                    return False

                heappop(len_heap) # We can remove it since it is valid

            # If we don't have anything in our heap or if we have
            # an equal number then we want to start a new subsequence
            if len(len_heap) == 0 or len_heap[0][0] == nums[i]:
                heappush(len_heap, [nums[i], 1])
            # Otherwise, we are at the start of the next subsequence and
            # want to add the next subsequent number into our heap
            else:
                curr, length = heappop(len_heap) # Current value and length of subsequence
                heappush(len_heap, [curr + 1, length + 1])

        # We want to add a check in for numbers that have a valid subsequence but aren't the
        # correct length. So for every remaining array, check the length of its subsequence
        for i in range(len(len_heap)):
            if len_heap[i][1] < 3:
                return False

        return True

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/1850131/Python-code-with-Heap