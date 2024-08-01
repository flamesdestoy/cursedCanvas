"""
This module provides the SubScreenFactory class.

classes:
    SubScreenFactory: Creator class with configuration paramerters
    of the product object.
"""
from ..sub_screens import SubScreen, SubScreenPool

class SubScreenFactory:
    """
    This is a factory class which specializes in creating and returning
    a sub screen object with the template configurations.

    props:
        width (int): How fat are the buffers (cols).
        height (int): How tall are the buffers (rows).

    Methods:
        create_pad: Returns an instantiate object.

    """

    def __init__(self, width: int, height: int, pool: SubScreenPool) -> None:
        self.width = width
        self.height = height
        self.pool = pool

    def create_sub_screen(self) -> SubScreen:
        """ Returns SubScreen instance! """

        pad = SubScreen(self.width, self.height)  # Instantiate pad
        
        self.pool.add_pad(pad)  # Register it at the pads pool
        return pad
