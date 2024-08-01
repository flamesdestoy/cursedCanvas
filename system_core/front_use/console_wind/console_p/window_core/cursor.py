"""
This module provides a class representing a screen cursor to draw 
components, with some operations to interact with the screens.

Classes:
    Cursor: A class to model a cursor object for rendering logic.
"""

# Built-in modules imports
from dataclasses import dataclass

# Local-coded modules imports
from .default_init_params import (
    DEFAULT_CURSOR_POSITION, DEFAULT_CURSOR_VISIBILITY
)

@dataclass
class Cursor:
    """
    A class modeling a CLI screen cursor.

    Attributes:
        __cursor_position (tuple[int, int]): Represent a pair of x, y axises coordinates in the screen.
        __cursor_visibility (bool): Wether we display the cursor styles or not.

    Methods:
        setters/getters
    """
    
    __cursor_position: tuple[int, int] = DEFAULT_CURSOR_POSITION
    __cursor_visibility: bool = DEFAULT_CURSOR_VISIBILITY

    @property
    def cursor_position(self) -> tuple[int, int]:
        return self.__cursor_position
    
    @cursor_position.setter
    def cursor_position(self, new_pos: tuple[int, int]) -> None:
        self.__cursor_position = new_pos

    @property
    def cursor_visibility(self) -> bool:
        return self.__cursor_visibility
    
    @cursor_visibility.setter
    def cursor_visibility(self, visibility: bool) -> None:
        if self.__cursor_visibility == visibility:  # Doing nothing for cursor
            return
        else:
            self.__cursor_visibility = visibility 
