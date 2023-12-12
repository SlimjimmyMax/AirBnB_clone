def calculate_square_sum(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    Parameters:
    - numbers (list): A list of numbers.

    Returns:
    - int: The sum of squares of the input numbers.
    """
    square_sum = sum(x**2 for x in numbers)
    return square_sum


if __name__ == "__main__":
    # Example usage:
    numbers_list = [1, 2, 3, 4, 5]
    result = calculate_square_sum(numbers_list)
    print(f"The sum of squares is: {result}")
