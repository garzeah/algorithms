const binary_search = function (arr, key) {
  let start = 0;
  let end = arr.length - 1;
  // Check is array is sorted in an ascending or descending fashion
  let isAscending = arr[start] < arr[end];

  while (start <= end) {
    middle = Math.floor((start + end) / 2);

    if (isAscending) {
      if (key < arr[middle]) end = middle - 1;
      else start = middle + 1;
    } else {
      if (key > arr[middle]) end = middle - 1;
      else start = middle + 1;
    }

    middle = Math.floor((start + end) / 2);
  }

  return arr[middle] === key ? middle : -1;
};

console.log(binary_search([4, 6, 10], 10));
console.log(binary_search([1, 2, 3, 4, 5, 6, 7], 5));
console.log(binary_search([10, 6, 4], 10));
console.log(binary_search([10, 6, 4], 4));
