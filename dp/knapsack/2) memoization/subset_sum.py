def can_partition(num, target):
   memo = [ [ -1 for x in range(target + 1) ] for y in range(len(num)) ]
   return helper(num, target, memo, 0)

def helper(num, target, memo, i):
   if target == 0:
      return True

   if target < 0 or i >= len(num):
      return False

   if memo[i][target] != -1:
      return memo[i][target]

   if num[i] <= target:
      if helper(num, target - num[i], memo, i + 1):
         memo[i][target] = True
         return memo[i][target]

   memo[i][target] = helper(num, target, memo, i + 1)
   return memo[i][target]
