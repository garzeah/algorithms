class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        result = []
        permutations = deque([[]])

        for curr_num in nums:
            # We will take all existing permutations and add
            # the current number to create new permutations
            n = len(permutations)
            for _ in range(n):
                old_permutation = permutations.popleft()
                # Create a new permutation by adding
                # the current number at every position
                for j in range(len(old_permutation) + 1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(j, curr_num)

                    if len(new_permutation) == nums_length:
                        result.append(new_permutation)
                    else:
                        permutations.append(new_permutation)

        return result

# Time Complexity
# We know that there are a total of N! permutations of a set
# with ‘N’ numbers. In the algorithm above, we are iterating
# through all of these permutations with the help of the two
# ‘for’ loops. In each iteration, we go through all the current
# permutations to insert a new number in them. To insert a
# number into a permutation of size ‘N’ will take O(N), which
# makes the overall time complexity of our algorithm O(N*N!).

# Space Complexity
# All the additional space used by our algorithm is for the
# result list and the queue to store the intermediate permutations.
# If you see closely, at any time, we don’t have more than N! permutations
# between the result list and the queue. Therefore the overall space
# complexity to store N! permutations each containing N elements will be O(N*N!).