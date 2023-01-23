# This is a 0/1 knapsack problem where each item can only be
# selected once, as we don't have multiple quantities of any item
def solve_knapsack(profits, weights, capacity):
  return helper(profits, weights, capacity, 0)

def helper(profits, weights, capacity, i):
    # Base cases
    if capacity <= 0 or i >= len(profits):
        return 0

    # Recursive call after choosing the element at the current index.
    # If the weight of the element at current index exceeds the
    # capacity, we shouldn't process this
    profit1 = 0
    if weights[i] <= capacity:
        profit1 = profits[i] + helper(profits, weights, capacity - weights[i], i + 1)

    # Recursive call after excluding the element at the current index
    profit2 = helper(profits, weights, capacity, i + 1)

    return max(profit1, profit2)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()

# Time Complexity: O(2^n), where ‘n’ represents the total number of items.
# This can also be confirmed from the above recursion tree. As we can see
# that we will have a total of ‘31’ recursive calls – calculated through
# (2^n) + (2^n) - 1, which is asymptotically equivalent to O(2^n).

# Space Complexity: The space complexity is O(n). This space will be used
# to store the recursion stack. Since our recursive algorithm works in a
# depth-first fashion, which means, we can’t have more than ‘n’
# recursive calls on the call stack at any time.