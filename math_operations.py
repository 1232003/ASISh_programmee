import math

def factorial(n):
  """
  Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.

  Raises:
    TypeError: If n is not an integer.
    ValueError: If n is a negative integer.
  """
  if not isinstance(n, int):
    raise TypeError("Input must be an integer.")
  if n < 0:
    raise ValueError("Input must be a non-negative integer.")
  if n == 0:
    return 1

  result = 1
  for i in range(1, n + 1):
    result *= i
  return result