var maxSlidingWindow = function (nums, k) {
  const dequeue = [];
  const output = [];

  for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
    // Making sure that the first value in the dequeue is the highest
    while (nums[windowEnd] > dequeue[dequeue.length - 1]) {
      dequeue.pop();
    }

    dequeue.push(nums[windowEnd]);

    // If our window overlaps the subarray length (k)
    if (windowEnd >= k - 1) {
      // Start finding the biggest number in our window
      output.push(dequeue[0]);

      // Remove maximum value when it is outside of
      // the start of our window
      if (nums[windowEnd - k + 1] === dequeue[0]) dequeue.shift();
    }
  }

  return output;
};
