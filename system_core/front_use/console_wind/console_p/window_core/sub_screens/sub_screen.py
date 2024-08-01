"""
This module is place of writing the SubScreen class for screen pads or 
( divisions and containers ), with some operations to interact with the
screens.

Classes:
    SubScreen: A class to model a screen pad with some interactions.
"""

# Importing sub screens components
from ..buffers import FrontBuffer, BackBuffer

class SubScreen:
    """
    A class to represent a curses pad (inner screen) in 2D surface.

    Attributes:
        front_buffer (FrontBuffer): The screen front buffer ( the displayable data portion ).
        back_buffer (BackBuffer): The screen back buffer ( the image flickering collapsor ).

    Methods:
        clear: Clears the front buffer's content.
        swap_buffer: swaps buffers contents.
    """

    _id_counter = 0
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._front_buffer = FrontBuffer(self._width, self._height)
        self._back_buffer = BackBuffer(width, height)
        self.idn = SubScreen._id_counter
        SubScreen._id_counter += 1

    def __str__(self) -> str:
        fb = f"width: {self._front_buffer.width}, height: {self._front_buffer.height}"
        bb = f"width: {self._back_buffer.width}, height: {self._back_buffer.height}"
        buffers_str = f"  Front Buffer: {fb}\n  Back Buffer: {bb}"
        
        return f"{buffers_str}"
    
    @classmethod
    def get_instance_count(cls):
        """Return the current count of instances."""
        return cls._instance_count
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, new_width: int) -> int:
        self._width = new_width

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, new_height: int) -> int:
        self._height = new_height

    @property
    def front_buffer(self) -> FrontBuffer:
        return self._front_buffer
    
    @front_buffer.setter
    def front_buffer(self, buffer) -> None:
        self._front_buffer = buffer

    @property
    def back_buffer(self) -> BackBuffer:
        return self._back_buffer
    
    @back_buffer.setter
    def back_buffer(self, buffer) -> None:
        self._back_buffer = buffer

    def _swap_buffers(self) -> None:
        self._front_buffer.grid, self._back_buffer.grid = self._back_buffer.grid, self._front_buffer.grid

    def write_text(self, row: int, col: int, text: str) -> None:
        """
        Writes text to the screen. 
        
        Does it by iterating over the inputed text, changes the 
        corresponding character situated by the row, column variables.
        Lastly, increments the positions by one by an algorithm.

        Args:
            row (int): Place in the y-axis.
            col (int): Place in the x-axis.
        """
        r, c = row, col  # Current position
        for char in text:
            if r >= self._height:  # If the row index goes out of bounds
                break
            if c >= self._width:  # If the column index goes out of bounds
                c = 0  # Move to the start of the next row
                r += 1
                if r >= self._height:  # If moving to the next row goes out of bounds
                    break
            self.back_buffer.modify_character(r, c, char)
            c += 1

        self._swap_buffers()
    
    def delete_character(self, row: int, col: int) -> None:
        """ Deletes character at position row, col. """
        self._back_buffer.delete_character(row, col)
        self._swap_buffers()

    def clear(self) -> None:
        """
        Resets and clears the front buffer 2D grid.

        This function does not take any arguments and does not return any value.
        """
        self._back_buffer.clear()
        self._swap_buffers()

    def clear_partition(self, start, end) -> None:
        """ 
        A method to clear a text from a starting position to an end.

        Args:
            start (tuple[int, int]): Starting axies text coordinates
            end (tuple[int, int]): Ending axies text coordinates
        """
        self._back_buffer.clear(start, end)

    def display_content(self) -> None:
        """ Prints the grid (front buffer). """
        self._front_buffer.display_grid()