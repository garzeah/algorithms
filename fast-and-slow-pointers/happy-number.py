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
            last_digit = num % 10 # Getting the last digit
            result += last_digit * last_digit # Squaring and adding the results
            num //= 10 # Getting the last digit

        return result

# Time Complexity: O(log(n))
# Space Complexity: O(1)