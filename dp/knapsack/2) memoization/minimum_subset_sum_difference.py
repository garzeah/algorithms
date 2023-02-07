def minimum_subarray_sum_difference(nums):
    memo = [ [ -1 for x in range(sum(nums) + 1) ] for y in range(len(nums)) ]
    return helper(nums, memo, 0, 0, 0)

def helper(nums, memo, sum1, sum2, i):
    if i >= len(nums):
        return abs(sum1 - sum2)

    if memo[i][sum1] != -1:
        return memo[i][sum1]

    # recursive call after including the number at the currentIndex in the first set
    diff1 = helper(nums, memo, sum1 + nums[i], sum2, i + 1)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = helper(nums, memo, sum1, sum2 + nums[i], i + 1)

    memo[i][sum1] = min(diff1, diff2)
    return memo[i][sum1]