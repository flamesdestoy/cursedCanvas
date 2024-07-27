"""
This module provides a class for managing console window elements and screens,
with some operations to interact with the screens.

Classes:
    ConsoleScreen: A class to model a console window with some interactions.
"""

from .cursor import Cursor
from .sub_screens import SubScreen

class ConsoleScreen:
    """
    Class modeling a console screen by storing properties and couple of
    methods. 

    Attributes:
        self._inner_screens (list[SubScreen]): List of sub windows.
        self._width (int): Represents the console screen width.
        self._height (int): Represents the console screen width.
        self.theme (str): Single variable used to recognize theme.
        self._cursor (Cursor): Screen cursor to write and perform data on wherever screen section.

    Methods:
        clear: Clears all the subscreens. Thus, having a black screen.
    """

    def __init__(self, inner_screens: list[SubScreen], width: int, height: int, theme="black") -> None:
        self._inner_screens = inner_screens
        self._width = width
        self._height = height  
        self.theme = theme
        self._cursor = Cursor()

    def __str__(self) -> str:
        size_str = f"\nwidth: {self._width} \nheight: {self._height}"
        pads_str = "".join([f"\npad {idx}: {pad}" for idx, pad in enumerate(self._inner_screens)])
        return f"Console window: {size_str}{pads_str}"

    @property
    def sub_screens(self) -> list[SubScreen]:
        return self._inner_screens
    
    @sub_screens.setter
    def sub_screens(self, screens: list[SubScreen]) -> str:
        self._inner_screens = screens
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def cursor(self) -> Cursor:
        return self._cursor
    
    def clear(self) -> None:  # Mops the sub screens front buffers
        for scr in self._inner_screens:
            scr.front_buffer.clear()