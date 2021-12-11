function binarySearch(arr, target) {
  let start = 0;
  let end = arr.length - 1;

  while (start <= end) {
    // As we update the start and end, have to
    // recalculate new middle
    let middle = Math.floor((start + end) / 2);

    if (target < arr[middle]) end = middle - 1;
    else if (target > arr[middle]) start = middle + 1;
    else return middle;
  }

  return -1;
}

console.log(binarySearch([2, 5, 6, 9, 13, 15, 28], 28));
console.log(binarySearch([28, 15, 13, 9, 6, 5, 2], 2));
