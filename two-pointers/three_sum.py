class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        triplets = []

        for i in range(len(arr)):
            # If we encounter a duplicate then skip
            if i > 0 and arr[i] == arr[i - 1]:
              continue

            left, right = i + 1, len(arr) - 1

            while(left < right):
                # These will be used to find a triplet that equals 0
                current_sum = arr[left] + arr[right]
                target_sum = -arr[i]

                # If we added current_sum and target_sum together
                # we would get 0
                if current_sum == target_sum:
                    triplets.append([-target_sum, arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # Preventing duplicates by checking if the previous
                    # values are the same number
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                # Since this is sorted it means we want a bigger current_sum
                elif target_sum > current_sum:
                    left += 1

                # Since this is sorted it means we want a smaller current_sum
                else:
                    right -= 1

        return triplets

# Time Complexity: O(n^2) b/c for every i, we are searching all of
# the values after it

# Space Complexity: O(n) bc we have to sort the array