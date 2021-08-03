const smallest_subarray_with_given_sum = function(s, arr) {
  let windowSum = 0, windowStart = 0, minLength = Infinity;

  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd];

    // Calculate minLength and start sliding the window
    while (windowSum >= s) {
      minLength = Math.min(minLength, windowEnd - windowStart + 1);

      // Slide the window
      windowSum -= arr[windowStart];
      windowStart++;
    }
  }

  return minLength;
};