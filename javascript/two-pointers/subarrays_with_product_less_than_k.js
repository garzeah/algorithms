if (k <= 1) return 0;
let windowStart = 0,
  count = 0,
  product = 1;

for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
  product = product * nums[windowEnd];

  // When our product is greater than k,
  // divide by value of windowStart and
  // slide the start window up
  while (product >= k) {
    product = product / nums[windowStart];
    windowStart += 1;
  }

  // Adding the count and the size of window
  count = count + (windowEnd - windowStart + 1);
}

return count;
