const triplet_sum_close_to_target = function (arr, targetSum) {
  arr.sort((a, b) => a - b);
  let smallestDiff = Infinity;

  for (let i = 0; i < arr.length; i++) {
    let left = i + 1,
      right = arr.length - 1;

    while (left < right) {
      let targetDiff = targetSum - arr[i] - arr[left] - arr[right];

      // We have the closest value to targetSum
      if (targetDiff === 0) return targetSum;

      // Keeps track of the smallest difference
      if (Math.abs(targetDiff) < Math.abs(smallestDiff))
        smallestDiff = targetDiff;

      if (targetDiff > 0) left++;
      // Need a triplet with a bigger sum
      else right--; // Need a triplet with a smaller sum
    }
  }

  // Gives us the sum of the triplet
  return targetSum - smallestDiff;
};
