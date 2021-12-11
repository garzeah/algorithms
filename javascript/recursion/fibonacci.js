var fib = function (n) {
  if (n === 0) return 0;
  else if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
};
