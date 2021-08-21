var reverseString = (s) => {
  function reverse(i, j) {
    if (i >= j) return;
    [s[i], s[j]] = [s[j], s[i]];
    reverse(i + 1, j - 1);
  }

  reverse(0, s.length - 1);
};
