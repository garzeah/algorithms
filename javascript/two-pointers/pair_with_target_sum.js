const pair_with_targetsum = function(arr, target_sum) {
  let left = 0, right = arr.length;

  while (left < right) {
    currSum = arr[left] + arr[right];
    if (target_sum === currSum) return [left, right];
    else if (target_sum > currSum) left++;
    else right--;
  }


  return [-1, -1];
}