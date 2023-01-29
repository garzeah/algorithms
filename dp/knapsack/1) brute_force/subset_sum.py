def can_partition(num, target):
   return helper(num, target, 0)

def helper(num, target, i):
   if target == 0:
      return True

   if target < 0 or i >= len(num):
      return False

   if num[i] <= target:
      if helper(num, target - num[i], i + 1):
         return True

   return helper(num, target, i + 1)
