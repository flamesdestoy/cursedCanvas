"""
This module configures and initializes the console window using the ConsolePopperFactory from the console_p module.

Imports:
- ConsolePopperFactory: Imported from the console_p module, this factory class is responsible for creating and managing console poppers.
- SCREEN_TITLE, MAIN_FILE_PATH, USE_TERMINAL: Imported from package_configs module, these constants are used for configuring the console window.

Variables:
- WINDOW_WIDTH: The width of the console window, obtained from the ConsolePopperFactory.
- WINDOW_HEIGHT: The height of the console window, obtained from the ConsolePopperFactory.

Details:
- The code creates an instance of ConsolePopperFactory.
- It uses this instance to create a console popper.
- The `popen_window` method is called with parameters `SCREEN_TITLE`, `MAIN_FILE_PATH`, and `USE_TERMINAL` to open a console window and retrieve its dimensions.

The `WINDOW_WIDTH` and `WINDOW_HEIGHT` variables store the dimensions of the opened console window, which can be used for further layout or display configurations.
"""
from console_p import ConsolePopperFactory
from .package_configs import (
    SCREEN_TITLE,
    MAIN_FILE_PATH,
    USE_TERMINAL
)

# Create an instance of ConsolePopperFactory
# Use the factory to create a console popper and open a window
# The window dimensions (width and height) are obtained from the popen_window method
WINDOW_WIDTH, WINDOW_HEIGHT = ConsolePopperFactory() \
                                                    .create_console_popper() \
                                                    .popen_window(
                                                        SCREEN_TITLE, 
                                                        MAIN_FILE_PATH, 
                                                        USE_TERMINAL
                                                    )