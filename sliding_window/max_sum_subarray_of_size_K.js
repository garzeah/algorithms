const max_sub_array_of_size_k = function(k, arr) {
  let maxSum = -Infinity, tempSum = 0;

  for (let i = 0; i < k; i++) {
    tempSum += arr[i];
  }

  maxSum = tempSum;

  for (let i = k; i < arr.length; i++) {
    tempSum += arr[i] - arr[i - k];
    maxSum = Math.max(tempSum, maxSum);
  }

  return maxSum;
};