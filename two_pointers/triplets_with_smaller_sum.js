const triplet_with_smaller_sum = function (arr, target) {
  arr.sort((a, b) => a - b);
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    count += search_pair(arr, target - arr[i], i + 1);
  }

  return count;
};

const search_pair = (arr, targetSum, left) => {
  let right = arr.length - 1,
    count = 0;

  while (left < right) {
    let currSum = arr[left] + arr[right];

    // Triplet with less than target sum
    if (currSum < targetSum) {
      // Since arr[right] >= arr[left], therefore, we can replace arr[right]
      // by any number between left and right to get a sum less than the target sum
      count += right - left;
      left++;
    } else {
      right--;
    } // We need a pair with a smaller sum
  }

  return count;
};
