const search_triplets = (arr) => {
  arr.sort((a, b) => a - b);
  const triplets = [];

  for (let i = 0; i < arr.length; i++) {
    // If we encounter a duplicate, skip
    if (i > 0 && arr[i] === arr[i - 1]) continue;
    search_pair(arr, -arr[i], i + 1, triplets);
  }

  return triplets;
};

const search_pair = (arr, target_sum, left, triplets) => {
  let right = arr.length - 1;

  while (left < right) {
    const curr_sum = arr[left] + arr[right];
    if (curr_sum === target_sum) {
      // Found the triplet
      triplets.push([-target_sum, arr[left], arr[right]]);
      left++;
      right--;
      // If we encounter duplicates, skip
      while (left < right && arr[left] === arr[left - 1]) left++;
      while (left < right && arr[right] === arr[right - 1]) right++;
    }
    // Need a pair w/ a bigger sum
    else if (target_sum > curr_sum) left++;
    // Need a pair w/ a smaller sum
    else right--;
  }
};
