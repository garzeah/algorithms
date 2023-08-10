class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))]
        stack = [] # pair: (temp, index)

        # Stack will be monotonically decreasing
        # since we're only keeping smaller numbers
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                output[stackIdx] = (i - stackIdx)

            stack.append((temp, i))

        return output

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=cTBiBSnjO3c