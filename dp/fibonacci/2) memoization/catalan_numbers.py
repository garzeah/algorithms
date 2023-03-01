def catalan(n):
  memo = {}
  return helper(n, memo)

def helper(n, memo):
  # Base case; C(0) = 1
  if n == 0 or n == 1:
    return 1

  # If n already evaluated, return from memo
  if n in memo:
    return memo[n]

  res = 0
  # Iterate from 1...n to evaluate: C(0) * C(n-1) + C(1) * C(n-2) ... + C(n-1)*C(0)
  for i in range(n):
     # C(i) * C(n-1-i)
    res += helper(i, memo) * helper(n-1-i, memo)

  # Store result in memo
  memo[n] = res
  return memo[n]

# TC/SC: O(n)