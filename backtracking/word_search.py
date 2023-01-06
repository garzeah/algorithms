class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        curr_path = set()

        def backtrack(row, col, i):
            if i >= len(word):
                return True

            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in curr_path or
                board[row][col] != word[i]
            ):
                return False


            curr_path.add((row, col))

            res = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row - 1, col, i + 1) or
                backtrack(row, col + 1, i + 1) or
                backtrack(row, col - 1, i + 1)
            )

            curr_path.remove((row, col))

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True

        return False