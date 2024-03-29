class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        return self.backtrack(n, 0, 0, [], output)

    def backtrack(self, n, opening, closing, curr_path, output):
        # We have found a valie parentheses
        if opening == closing == n:
            output.append("".join(curr_path))
            return

        # Only can add opening parentheses as long as it's < n
        if opening < n:
            curr_path.append('(')
            self.backtrack(n, opening + 1, closing, curr_path, output)
            curr_path.pop()

        # Only can add closing parentheses as long as it's < opening
        if closing < opening:
            curr_path.append(')')
            self.backtrack(n, opening, closing + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(N * 2^n) because let’s try to estimate how many
# combinations we can have for ‘N’ pairs of balanced parentheses.
# If we don’t care for the ordering - that ) can only come after
# ( - then we have two options for every position, i.e., either
# put open parentheses or close parentheses. This means we can
# have a maximum of 2^N combinations. Because of the ordering,
# the actual number will be less than 2^N. Also, we need to
# concatenate each string which would take O(n).

# Space Complexity: O(N * 2^n)

# Solution: https://www.youtube.com/watch?v=s9fokUqJ76A