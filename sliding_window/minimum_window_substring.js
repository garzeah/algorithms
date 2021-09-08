var minWindow = function (str, pattern) {
  let windowStart = 0,
    substrStart = 0,
    matched = 0,
    minLength = Infinity;
  const charFreq = {};

  // Getting a freqMap of the pattern
  for (let char of pattern) {
    if (!(char in charFreq)) charFreq[char] = 0;
    charFreq[char]++;
  }

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightChar = str[windowEnd];

    if (rightChar in charFreq) {
      charFreq[rightChar]--;
      // Counts every matching character
      if (charFreq[rightChar] >= 0) matched += 1;
    }

    // Shrink the window if we can, finish as soon as we remove a matched character
    while (matched === pattern.length) {
      if (minLength > windowEnd - windowStart + 1) {
        minLength = Math.min(minLength, windowEnd - windowStart + 1);
        substrStart = windowStart;
      }

      const leftChar = str[windowStart];
      windowStart++;

      // Note that we could have extra matching characters, therefore
      // we'll decrement the matched count if a matched character
      // is going out of the window
      if (leftChar in charFreq) {
        if (charFreq[leftChar] === 0) matched -= 1;
        charFreq[leftChar]++;
      }
    }
  }

  // We never found a minLength < str.length
  if (minLength > str.length) return "";

  // Returning the beginning of the window and
  return str.substring(substrStart, substrStart + minLength);
};
