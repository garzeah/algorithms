class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])

        for row in image:
            for i in range((n + 1) // 2): # Getting the amount of times we need to swap
                # Swapping the values and getting the inverted image using XOR
                row[i], row[n - 1 - i] = row[n - 1 - i] ^ 1, row[i] ^ 1

        return image

# Time Complexity: O(n)
# Space Complexity: O(1)