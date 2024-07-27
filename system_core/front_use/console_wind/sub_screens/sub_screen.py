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

    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._front_buffer = FrontBuffer(self._width, self._height)
        self._back_buffer = BackBuffer(width, height)

    def __str__(self) -> str:
        size_str = f"  width: {self._width}  height: {self._height}"
        fb = f"width: {self._front_buffer.width}, height: {self._front_buffer.height}"
        bb = f"width: {self._back_buffer.width}, height: {self._back_buffer.height}"
        buffers_str = f"  Front Buffer: {fb}  Back Buffer: {bb}"
        
        return f"{size_str}{buffers_str}"
    
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

    def swap_buffers(self) -> None:
        self._front_buffer.grid, self._back_buffer.grid = self._back_buffer.grid, self._front_buffer.grid

    def write_text(self, row: int, col: int, text: str) -> None:
        # Write whatever on the back buffer
        # Swap buffers to get smooth transaction
        pass
    
    def delete_character(self, row: int, col: int) -> None:
        pass

    def clear(self) -> None:
        """
        Resets and clears the front buffer 2D grid.

        This function does not take any arguments and does not return any value.
        """
        self._front_buffer.clear()

    def display_content(self) -> None:
        self._front_buffer.display_grid()