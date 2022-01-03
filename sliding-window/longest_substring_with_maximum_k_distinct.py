# Longest Substring with Maximum K Distinct Characters
def longest_substring_with_k_distinct(str1, k):
  start, max_length, freq = 0, float('-inf'), {}

  for end in range(len(str1)):
    rightElem = str1[end]

    if rightElem not in freq:
      freq[rightElem] = 0
    freq[rightElem] += 1

    # shrink the sliding window, until we are left
    # with 'k' distinct characters in freq_map
    while (len(freq) > k):
      leftElem = str1[start]
      freq[leftElem] -= 1

      if freq[leftElem] == 0:
        del freq[leftElem]

      start += 1

    max_length = max(max_length, end - start + 1)

  return max_length

# Time Complexity: The outer for loop runs for all
# characters, and the inner while loop processes
# each character only once; therefore, the time
# complexity of the algorithm will be O(N+N), which
# is asymptotically equivalent to O(N).

# Space Complexity: O(K) where K is the amount of
# distinct characters