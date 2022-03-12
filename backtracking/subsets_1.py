class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start by initializing our subsets and adding an empty subset
        subsets = []
        subsets.append([])

        for curr_num in nums:
            # We will take all existing subsets and insert
            # the current number in them to create new subsets
            n = len(subsets)
            for i in range(n):
                # Create a new subset from the existing subset
                # and insert the current element to it
                temp_set = list(subsets[i])
                temp_set.append(curr_num)
                subsets.append(temp_set)


        return subsets

# Time Complexity: Since, in each step, the number of subsets doubles as we add
# each element to all the existing subsets, therefore, we will have a total of
# O(2^N) subsets, where ‘N’ is the total number of elements in the  input set.
# And since we construct a new subset from an existing set, therefore, the
# time complexity of the above algorithm will be O(N*2^N)

# Space Complexity: All the additional space used by our algorithm is for the
# output list. Since we will have a total of O(2^N) subsets, and each subset
# can take up to O(N) space, therefore, the space complexity of our
# algorithm will be O(N*2^N)