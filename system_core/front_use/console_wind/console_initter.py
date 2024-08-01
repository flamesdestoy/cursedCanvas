"""
Module for initializing console window components.

This module provides the `ConsoleInitializer` class, which is responsible for 
creating and setting up the main console window and any sub screens needed 
for the application. It utilizes factory classes from the `x.window_core.window_factory` 
module to create these components.

Classes:
    ConsoleInitializer: Handles the initialization of console window elements.
"""

# Import factories
from console_p import (
    ConsoleScreenFactory,
    SubScreenFactory
)
# Import configuration data
from dummy_configs import SCREEN_CONFIGS, PADS_CONFIGS

class ConsoleInitializer:
    """
    A class responsible for initializing and setting up the console window and sub screens.

    Attributes:
        __console_screen_factory (ConsoleScreenFactory): Factory instance
        to create console screens.
        __pads_factory (SubScreenFactory): Factory instance to create sub
        screens.
    """

    def __init__(self) -> None:
        self.__console_screen_factory = ConsoleScreenFactory(*SCREEN_CONFIGS)
        self.__pads_factory = SubScreenFactory(*PADS_CONFIGS)
        # Other factory if caching system included
    
    def init_console(self):
        """
        This method creates the console window and a sub screen.

        This method uses the factory instances to create and set up the main console window 
        and a sub screen. It returns these components as a tuple.

        Returns:
            tuple: A tuple containing the ConsoleScreen and SubScreen instances.
        """

        # Products creations
        console_window = self.__console_screen_factory.create_screen()
        self.__pads_factory.create_sub_screen()

        return console_window
    
