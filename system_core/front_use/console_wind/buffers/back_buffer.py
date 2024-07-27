"""
This module provides a concrete class for managing the screen's back 
buffer.

Classes:
    BackBuffer: Sub class is a back buffer with a 2DArray.
"""
from dataclasses import dataclass

from .abstract_buffer import Buffer
from ..utils.buffers_utils import create_grid
from ..data_configs import (
    MAX_BACK_BUFFER_WIDTH,
    MAX_BACK_BUFFER_HEIGHT,
    ADJUSTMENT_RANGE_TOP
)

@dataclass
class BackBuffer(Buffer):
    """
    A class representing a back buffer, extending the Buffer abstract class.
    Reducing flickering, increasing the image rendering speed freshly.

    Attributes:
        __viewport_cache (Cache): Memory store that is used in scrolling feature implmentation
        
    Methods:
        init_buffer: Realization OOP concept.
    """
    
    def init_buffer(self) -> None:
        """ 
        Implementation of init_buffer abstract method to initialize a 2DArray!

        Using method overloading and overriding of polymorphism concept to create a grid of characters after performing some logic and calculations.
        Setting the grid's size the same as the front buffer's size if it is in our expantion limits, otherwise we create the grid with a default size which is samller than the expantion limits.

        This function does not take any arguments and does not return any value.
        """
        
        front_buffer_size = self._width*self._height
        creation_params = ()

        # Sees if the front buffer is in the negotiable adjustment range
        if front_buffer_size <= ADJUSTMENT_RANGE_TOP:
            # Create the back buffer's grid with the front buffer's dimensions to be equal
            creation_params = (
                self._width, 
                self._height,
                self.grid_char
            )
        else:
            # Create the back buffer 2D array grid with the maximum preset dimensions values 
            creation_params = (
                MAX_BACK_BUFFER_WIDTH, 
                MAX_BACK_BUFFER_HEIGHT, 
                self.grid_char
            )

        self._grid = create_grid(*creation_params)  # grid creation

    def resize(self) -> None:
        pass
