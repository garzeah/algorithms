# String Anagrams
def find_string_anagrams(str1, pattern):
  start, matched = 0, 0
  pattern_freq = {}
  result_indexes = []

  for char in pattern:
    if char not in pattern_freq:
      pattern_freq[char] = 0
    pattern_freq[char] += 1

  # Our goal is to match all the characters from the 'pattern_freq'
  # with the current window try to extend the range [start, end]
  for end in range(len(str1)):
    right_char = str1[end]

    if right_char in pattern_freq:
      # Decrement the frequency of matched character
      pattern_freq[right_char] -= 1
      if pattern_freq[right_char] == 0:
        matched += 1

    if len(pattern_freq) == matched:
      result_indexes.append(start)

    # Shrink the sliding window
    if end >= len(pattern) - 1:
      left_char = str1[start]
      start += 1

      if left_char in pattern_freq:
        if pattern_freq[left_char] == 0:
          matched -= 1 # Before putting the character back, decrement the matched count
        pattern_freq[left_char] += 1 # Put the character back

  return result_indexes

