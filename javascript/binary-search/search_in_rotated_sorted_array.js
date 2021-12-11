let start = 0;
let end = arr.length - 1;

while (start <= end) {
  mid = Math.floor((start + end) / 2);

  if (arr[mid] === key) return mid;

  if (arr[start] <= arr[mid]) {
    // Left side is sorted in ascending order
    if (key >= arr[start] && key < arr[mid]) {
      end = mid - 1;
    } else {
      // key > arr[mid]
      start = mid + 1;
    }
  } else {
    // Right side is sorted in ascending order
    if (key > arr[mid] && key <= arr[end]) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
}

// We are not able to find the element in the given array
return -1;
