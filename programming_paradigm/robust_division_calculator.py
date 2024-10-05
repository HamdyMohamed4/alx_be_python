def safe_divide(numerator, denominator):
  """
  Safely performs division handling potential errors for division by zero and non-numeric input.

  Args:
      numerator: The number to be divided (numerator).
      denominator: The number to divide by (denominator).

  Returns:
      A string message indicating error or the result of the division as a float.
  """
  try:
    # Attempt to convert arguments to floats for division
    numerator = float(numerator)
    denominator = float(denominator)
    result = numerator / denominator
    return f"The result of the division is {result:.2f}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Please enter numeric values only."