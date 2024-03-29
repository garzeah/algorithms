class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.shelfWidth = shelfWidth # For when we want to fill a new bookshelf
        dp = [[-1 for x in range(shelfWidth + 1)] for y in range(len(books))]
        return self.helper(books, 0, shelfWidth, 0, dp)

    def helper(self, books, i, width, height, dp):
        if i >= len(books):
            return height

        if dp[i][width] == -1:
            # Choice1: Fill current bookshelf
            choice1 = float('inf')
            if books[i][0] <= width:
                choice1 = self.helper(books, i + 1, width - books[i][0], max(height,books[i][1]), dp)

            # Choice-2: Start filling new book-shelf with
            # previous height considered
            choice2 = height + self.helper(books, i + 1, self.shelfWidth - books[i][0], books[i][1], dp)


            dp[i][width] = min(choice1, choice2)

        return dp[i][width]

