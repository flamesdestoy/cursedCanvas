"""
This module provides the ConsoleScreenFactory class.

classes:
    ConsoleScreenFactory: Creator class with configuration paramerters
    of the ConsoleScreen product object.
"""
from ..sub_screens import SubScreenPool
from ..console_screen import ConsoleScreen

class ConsoleScreenFactory:
    """
    This is a factory class specializes in creating and returning
    a console screen instance with the template configurations.

    props:
        width (int): How fat are the buffers (cols).
        height (int): How tall are the buffers (rows).

    Methods:
        create_pad: Returns an instantiate object.

    """

    def __init__(self, title: str, width: int, height: int, pads: SubScreenPool) -> None:
        self._title = title
        self._width = width
        self._height = height
        self._pads = pads

    def create_screen(self) -> ConsoleScreen:
        """ Returns ConsoleScreen instance! """

        return ConsoleScreen(self._title, self._width, self._height, self._pads)