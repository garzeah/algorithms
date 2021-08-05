const length_of_longest_substring = function (str, k) {
  let windowStart = 0,
    maxLength = -Infinity,
    maxRepeat = -Infinity,
    freqMap = {};

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightChar = str[windowEnd];

    if (!(rightChar in freqMap)) freqMap[rightChar] = 0;
    freqMap[rightChar]++;

    // Keeps track of the maximum repeating letter in any window
    maxRepeat = Math.max(maxRepeat, freqMap[rightChar]);

    // Subtracting size of the current window with maxRepeat to get
    // the remaining letters (that is non-repeating), if our
    // remaining letters is greater than 'k' then we have
    // to shrink the window
    if (windowEnd - windowStart + 1 - maxRepeat > k) {
      const leftChar = str[windowStart];
      freqMap[leftChar]--;
      windowStart++;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }

  return maxLength;
};
