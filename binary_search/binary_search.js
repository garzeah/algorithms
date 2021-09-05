function binarySearch(arr, target) {
  let start = 0,
    end = arr.length - 1,
    middle = Math.floor((start + end) / 2);

  while (start <= end) {
    if (target < arr[middle]) end = middle - 1;
    else start = middle + 1;

    // As we update the start and end, have to
    // recalculate new middle
    middle = Math.floor((start + end) / 2);
  }

  if (arr[middle] !== target) return -1;

  return middle;
}

console.log(binarySearch([2, 5, 6, 9, 13, 15, 28], 28));
console.log(binarySearch([28, 15, 13, 9, 6, 5, 2], 2));
