"""
This module provides an abstract class for managing screen canvas,
with some operations to interact with the canvas.

Classes:
    Buffer: An abstract class templating a screen buffer with a 2DArray.
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# Configuration data, utility functions imported 
from ..data_configs import DEFAULT_GRID_CHAR
from ..utils.buffers_utils import validate_grid

@dataclass
class Buffer(ABC):
    """
    A simple abstract class templating a screen buffer with a 2DArray. 

    Attributes:
        _width (int): Dimension for the grid 2D arrays
        _height (int): Dimension for the grid 2D arrays
        _grid (list): The 2D list that stores nested arrays with array elements.
    
    Methods:
        access_character: returns a nested array element (character) with type str at given position.
        modify_character: changes a nested array element (character) value to a passed in str argument and pos.
        remove_character: deletes a nested array element (character) with the given position.
        clear: Resets and initializes the 2D grid with default characters (clears the grid).

        init_buffer: abstract method to implement by subclasses to initialize a buffer's grid.
    """
    _width: int
    _height: int
    _grid: list[list[str]] = field(init=False, repr=False)
    grid_char: str = DEFAULT_GRID_CHAR

    def __post_init__(self) -> None:
        self.init_buffer()

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height

    @property
    def grid(self) -> list[list[str]]:
        return self._grid
    
    @grid.setter
    def grid(self, new_grid: list[list[str]]) -> None:
        if not validate_grid(new_grid):  # Checking for the grid's rectangular shape
            raise Exception("Grid is not a rectangle! Refactor your grid.")
        
        # Setting the new grid object
        self.set_grid_object(new_grid, self._height, self._width)
        
    def set_grid_object(self, new_grid, new_height, new_width):  # Extracted method
        self._grid = new_grid
        self._height = new_height
        self._width = new_width

    def access_character(self, row: int, col: int) -> str:
        """ Returns a character by the given coordinates """

        # Validating the character coordinates
        if not (0 <= row < self._height):
            return IndexError("Row value is out of bounds!")
        
        if not (0 <= col < self._width):
            return IndexError("Column value is out of bounds!")
        
        return self._grid[row][col]
    
    def modify_character(self, row: int, col: int, new_char: str):
        """ Modifies a character value in the canvas """

        # Validating the character coordinates
        if row >= self._height:
            raise IndexError(f"Row index {row} is out of range.")
        
        if col >= self._width:
            raise IndexError(f"Column index {col} is out of range.")
        
        # Resets a value of the selected character
        self._grid[row][col] = new_char

    def delete_character(self, row: int, col: int) -> None:
        """ Deletes a character """

        # Validating the character coordinates
        if row >= self._height:
            return IndexError("Row value is out of bounds!")
        
        if col >= self._width:
            return IndexError("Column value is out of bounds!")

        # removing the selected character        
        self._grid[row][col] = self.grid_char

    def clear(self, starting_pos=(0, 0), finishing_pos=(-1, -1)) -> None:
        """ Method to clear the entire canvas! """

        starting_row, starting_col = starting_pos  # un-packing tuple
        finishing_row, finishing_col = finishing_pos  # un-packing tuple

        rows_num = self._height  # Varible renaming
        cols_num = self._width  # Variable renaming

        # Handle negative indecies
        if finishing_row < 0:
            finishing_row += rows_num
        
        if finishing_col < 0:
            finishing_col += cols_num

        # Validating the inputs (canvas portion start, end coordinates)
        if starting_row < 0 or starting_row >= self._height:
            return IndexError("The starting row value is out of bounds!")
                
        if starting_col < 0 or starting_col >= len(self._grid[starting_row]):
            return IndexError("The starting column value is out of bounds!")
        
        if finishing_row >= self._height:
            return IndexError("The finishing row value is out of bounds!")
               
        if finishing_col >= len(self._grid[starting_row]):
            return IndexError("The finishing column value is out of bounds!")
        
        # Reinitializing the canvas to the default character
        for row in range(starting_row, finishing_row):
            for col in range(starting_col, finishing_col):
                self._grid[row][col] = DEFAULT_GRID_CHAR  # Clearing characters
    
    def display_grid(self) -> None:
        for row in self._grid:
            print(''.join(map(str, row)))
    
    @abstractmethod
    def init_buffer(self) -> None:
        pass