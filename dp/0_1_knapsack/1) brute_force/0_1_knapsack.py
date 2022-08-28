def solve_knapsack(profits, weights, capacity):
    return helper(profits, weights, capacity, 0)

def helper(profits, weights, capacity, start):
    # Base checks
    if capacity <= 0 or start >= len(profits):
        return 0

    # recursive call after choosing the element at the start
    # if the weight of the element at start exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[start] <= capacity:
        profit1 = profits[start] + helper(profits, weights, capacity - weights[start], start + 1)

    # recursive call after excluding the element at the start
    profit2 = helper(profits, weights, capacity, start + 1)

    return max(profit1, profit2)

# Time Complexity: O(2^n), where ‘n’ represents the total number of items.
# This can also be confirmed from the above recursion tree. As we can see
# that we will have a total of ‘31’ recursive calls – calculated through
# (2^n) + (2^n) - 1, which is asymptotically equivalent to O(2^n).

# Space Complexity: The space complexity is O(n). This space will be used
# to store the recursion stack. Since our recursive algorithm works in a
# depth-first fashion, which means, we can’t have more than ‘n’
# recursive calls on the call stack at any time.