const longest_substring_with_k_distinct = function(str, k) {
  let windowStart = 0, maxLength = -Infinity, freq = {};

  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    let rightChar = str[windowEnd];

    if (!(rightChar in freq)) freq[rightChar] = 0;
    freq[rightChar]++;

    // If we are over K then let's shrink the window
    while (Object.keys(freq).length > k) {
      // Want to make sure we have <= K keys
      let leftChar = str[windowStart];
      freq[leftChar]--;
      if (freq[leftChar] === 0) delete freq[leftChar];

      // Move up the start of the window
      windowStart++;
    }

    // Calculate the maxLength now that we've met out criteria of <= K keys
    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }
  
  return maxLength;
};
