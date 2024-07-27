"""
This module provides a concrete class for managing the screen's front 
buffer user interface of the screen.

Classes:
    FrontBuffer: Sub class is a front buffer to print to the user.
"""
from dataclasses import dataclass

from .abstract_buffer import Buffer
from ..utils.buffers_utils import create_grid

@dataclass
class FrontBuffer(Buffer):
    """
    A class representing a front buffer, extending the Buffer abstract class. 

    Attributes:
        __viewport_cache (Cache): Memory store that is used in scrolling feature implmentation
        
    Methods:
        init_buffer: Realization OOP concept.
    """
    __viewport_cache: str = "Caching dependencies"

    def init_buffer(self) -> None:
        """ 
        Implementation of init_buffer abstract method to create and initialize 2DArray!
        
        Returns:
            None: nothing!
        """
        self._grid = create_grid(self._width, self._height, self.grid_char)  # grid creation