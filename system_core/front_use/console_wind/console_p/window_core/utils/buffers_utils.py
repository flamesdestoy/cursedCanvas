"""
This module provides some utilities functions to perform operations and
manage 2D matrix related operations.

Functions:
    create_grid: Function to create a 2D array filled with characters.
    validate_grid: Function which checks if a 2D array is rectangular.
"""

# Buffer grid creation
def create_grid(width: int, height: int, fill_char: str):
    """
    Creates a 2D array by expected parameters.

    Args:
        width (int): The wanted grid width value.
        height (int): The wanted grid height value.
        fill_char (str): A character to represent nested list values.

    Returns:
        list: A list of lists containing passed in characters.
    """
    return [
            [fill_char for _ in range(width)] 
            for _ in range(height)
        ]

# Grid validation
def validate_grid(grid: list[list[str]]) -> bool:
    """
    Checks if the passed in grid is consistent, in a rectangular shape.

    The function sees if the passed in grid is a rectangle by checking the length of rows and the length 
    of columns is the same length of columns in all of the rows.

    Args:
        grid (list[list[str]]): A nested arrays storing characters.

    Returns:
        bool: A true or false value is outputed.
    """

    if not grid:
        return True  # An empty grid is considered valid

    first_row_length = len(grid[0])
    for row in grid[1:]:  # Start iterating from the second row
        if len(row) != first_row_length:
            return False
    return True
