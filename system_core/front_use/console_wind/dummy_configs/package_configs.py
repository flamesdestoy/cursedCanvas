"""
This module sets up the configuration for the screen, including title, file paths, and screen dimensions.
It also imports necessary components and defines constants used throughout the application.

Imports:
- PADS_POOL: Imported from the pads_pool module to manage padding configurations.
- WINDOW_WIDTH and WINDOW_HEIGHT: Imported from the window_size module to define screen dimensions.

Constants:
- SCREEN_TITLE: The title of the screen or window.
- MAIN_FILE_PATH: The file path to the main script or module.
- USE_TERMINAL: A flag indicating whether to use a terminal or command-line interface.
- SCREEN_CONFIGS: A tuple containing screen configurations including title, width, height, and padding pool.
"""
from .pads_pool import PADS_POOL

SCREEN_TITLE = "New Screen, Last Era!"  # Title of the screen or Command Prompt window
MAIN_FILE_PATH = "C:/Users/flame/OneDrive/Desktop/prg_env/f.py"  # File path to the main script or module
USE_TERMINAL = True  # Flag to determine whether to use a terminal or not

from .window_size import WINDOW_WIDTH, WINDOW_HEIGHT

# Tuple containing screen configurations
# It includes:
# - SCREEN_TITLE: The title for the screen or window.
# - WINDOW_WIDTH: The width of the screen/window.
# - WINDOW_HEIGHT: The height of the screen/window.
# - PADS_POOL: Padding configurations or settings for the screen.
SCREEN_CONFIGS = (SCREEN_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, PADS_POOL)
