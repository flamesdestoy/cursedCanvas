"""
This module defines a class to deal with some of the console screen 
components.

Classes:
    SubScreenPool: Class for grouping and caching subscreens instances.
"""

from dataclasses import dataclass, field

from .sub_screen import SubScreen

@dataclass
class SubScreenPool:
    """
    This is the caching pool of the subscreens used in the console.

    It stores the pads in an array and treats them independantly.

    Properties:
        __sub_screens (dict[identifier, SubScreen]): Stores pads.
    
    Methods:
        get_screens: Returns the property __sub_screens.
        add_pad: Appends a subscreen to the array they are stored in.
        remove_pad: Deletes and the removes the selected pad.
    """

    _instance: 'SubScreenPool' = field(default=None, init=False, repr=False)
    __sub_screens: dict[int, SubScreen] = field(default_factory=dict, init=False)

    def __post_init__(self):
        if SubScreenPool._instance is None:
            SubScreenPool._instance = self
        else:
            raise RuntimeError("This class is a singleton!")

    @classmethod
    def get_instance(cls) -> 'SubScreenPool':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def sub_screens(self) -> dict[int, SubScreen]:
        return self.__sub_screens
    
    def get_pad(self, pad: SubScreen) -> SubScreen:
        """ Returns the sub screen object! """

        sub_screen = self.__sub_screens.get(pad.idn)

        return sub_screen if sub_screen else None
    
    def get_items(self) -> dict[int, SubScreen]:
        """ Returns the pool's elements! """
        return self.__sub_screens.items()
    
    def add_pad(self, pad: SubScreen) -> None:
        """
        This method appends the inputed pad value (sub screen) to the
        array.

        Args:
            pad (SubScreen): Represents the sub screen.
        """
        
        # Allocating and assigning the pad to its position
        self.__sub_screens[pad.idn] = pad
    
    def add_pads(self, *pads) -> None:
        """
        Registers the passed in sub screens into the pool!
        Args:
            pads (SubScreen): positional arguments passed in.
        """
        for pad in pads:
            self.add_pad(pad)  # Adding sub screens to pool

    def remove_pad(self, pad: SubScreen) -> None:
        """
        This method appends the inputed pad value (sub screen) to the
        array.

        Args:
            pad (SubScreen): Represents the sub screen the method removes.
        """
        popped_item = self.__sub_screens.pop(pad.idn)  # Remove screen from pool
        del popped_item # Deleting the screen object
    
    def remove_pads(self, *pads) -> None:
        """
        Deletes the passed in sub screens from the pool and memory!
        Args:
            pads (SubScreen): positional arguments passed in.
        """
        for pad in pads:
            self.remove_pad(pad)

    def clear_pool(self) -> None:
        """ For clearing the pool! """
        self.__sub_screens.clear()
