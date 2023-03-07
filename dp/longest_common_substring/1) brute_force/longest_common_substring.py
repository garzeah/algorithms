def lcs_length(s1, s2):
  return helper(s1, s2, 0, 0, 0)

def helper(s1, s2, i, j, count):
  # Base case of when either string has been exhausted
  if i >= len(s1) or j >= len(s2):
    return count

  # If i and j characters match, increment the
  # count and compare the rest of the strings
  if s1[i] == s2[j]:
    count = helper(s1, s2, i + 1, j + 1, count + 1)

  # Compare s1[i:] with s2, s1 with s2[j:], and
  # take max of current count and these two results
  return max(count, helper(s1, s2, i + 1, j, 0), helper(s1, s2, i, j + 1, 0))

# TC: O(3^(m + n))
# SC: O(m + n)