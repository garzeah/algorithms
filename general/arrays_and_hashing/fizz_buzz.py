class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [None] * n

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                output[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                output[i - 1] = "Fizz"
            elif i % 5 == 0:
                output[i - 1] = "Buzz"
            else:
                output[i - 1] = str(i)

        return output

# Time Complexity: O(n)
# Space Complexity: O(n)