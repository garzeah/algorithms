const fruits_into_baskets = function(fruits) {
  let windowStart = 0, maxLength = -Infinity, freq = {};

  for (let windowEnd = 0; windowEnd < fruits.length; windowEnd++) {
    let rightFruit = fruits[windowEnd];

    if (!(rightFruit in freq)) freq[rightFruit] = 0;
    freq[rightFruit]++;

    // We only want at most 2 fruits in the basket
    while (Object.keys(freq).length > 2) {
      let leftFruit = fruits[windowStart];

      // Shrink the window
      freq[leftFruit]--;
      if (freq[leftFruit] === 0) delete freq[leftFruit];
      windowStart++;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }

  return maxLength;
};