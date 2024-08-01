"""
This module provides a class for managing console window elements and screens,
with some operations to interact with the screens.

Classes:
    ConsoleScreen: A class to model a console window with some interactions.
"""

from .cursor import Cursor
from .sub_screens import SubScreenPool

class ConsoleScreen:
    """
    Class modeling a console screen by storing properties and couple of
    methods. 

    Attributes:
        self._sub_screens_pool (list[SubScreen]): List of sub windows.
        self._width (int): Represents the console screen width.
        self._height (int): Represents the console screen width.
        self.theme (str): Single variable used to recognize theme.
        self._cursor (Cursor): Screen cursor to write and perform data on wherever screen section.

    Methods:
        clear: Clears all the subscreens. Thus, having a black screen.
    """

    def __init__(self, title: str, width: int, height: int, sub_screens: SubScreenPool, theme="black") -> None:
        self.__title = title
        self._width = width
        self._height = height
        self._sub_screens_pool = sub_screens
        self.theme = theme
        self._cursor = Cursor()

    def __str__(self) -> str:
        size_str = f"\nwidth: {self._width} \nheight: {self._height}"
        pads_str = "".join([f"\npad {idn}: {pad}" for idn, pad in self._sub_screens_pool.get_items()])
        return f"Console window: {size_str}{pads_str}"

    @property
    def title(self) -> int:
        return self.__title
    
    @title.setter
    def title(self, new_title: str) -> int:
        self.__title = new_title
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def sub_screens(self) -> SubScreenPool:
        return self._sub_screens_pool
    
    @sub_screens.setter
    def sub_screens(self, screens: SubScreenPool) -> None:
        self._sub_screens_pool = screens
    
    @property
    def cursor(self) -> Cursor:
        return self._cursor
    
    def clear(self) -> None:  # Mops the sub screens front buffers
        for _, scr in self._sub_screens_pool.get_items():
            scr.clear()
