class Solution:
    def isHappy(self, num: int) -> bool:
        slow, fast = num, num

        while True:
            slow = self.find_square_sum(slow) # Move one step
            fast = self.find_square_sum(self.find_square_sum(fast)) # Move two steps

            if slow == fast:  # Found the cycle
                break

        return slow == 1  # See if the cycle is stuck on the number '1'

    # Logic to check if its a happy number
    def find_square_sum(self, num):
        result = 0

        while num > 0:
            last = num % 10
            result += last * last
            num = num // 10

        return result

# Time Complexity: O(log(n))
# Space Complexity: O(1)