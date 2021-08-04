const non_repeat_substring = function (str) {
  let windowStart = 0,
    freq = {},
    maxLength = -Infinity;

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightChar = str[windowEnd];

    if (rightChar in freq) {
      // We want windowStart to slide up to the repeating character
      // so we can start counting the max no-repeat substring
      windowStart = Math.max(windowStart, freq[rightChar] + 1);
    }

    // Want to keep track of the position of the character
    freq[rightChar] = windowEnd;

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }

  return maxLength;
};
