const length_of_longest_substring = function (str, k) {
  let windowStart = 0,
    maxLength = -Infinity,
    maxRepeat = -Infinity,
    freqMap = {};

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightElem = str[windowEnd];

    if (!(rightElem in freqMap)) freqMap[rightElem] = 0;
    freqMap[rightElem]++;

    // Keeps track of the maximum repeating letter in any window
    maxRepeat = Math.max(maxRepeat, freqMap[rightElem]);

    // Subtracting size of the current window with maxRepeat to get
    // the remaining letters (that is non-repeating), if our
    // remaining letters is greater than 'k' then we have
    // to shrink the window
    if (windowEnd - windowStart + 1 - maxRepeat > k) {
      const leftElem = str[windowStart];
      freqMap[leftElem]--;
      windowStart++;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }

  return maxLength;
};
