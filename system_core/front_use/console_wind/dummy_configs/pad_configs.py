"""
This module sets up configuration constants related to padding and window size.

Imports:
- PADS_POOL: Imported from the pads_pool module, this contains padding configurations used for layout management.
- WINDOW_WIDTH: Imported from the window_size module, this defines the width of the window or screen.
- WINDOW_HEIGHT: Imported from the window_size module, this defines the height of the window or screen.

Constants:
- PADS_CONFIGS: A tuple that aggregates window dimensions and padding configurations. 
  It includes:
  - WINDOW_WIDTH: The width of the window/screen.
  - WINDOW_HEIGHT: The height of the window/screen.
  - PADS_POOL: Padding configurations used in the layout.
"""
from .pads_pool import PADS_POOL
from .window_size import WINDOW_WIDTH, WINDOW_HEIGHT

# Tuple containing window dimensions and padding configurations
# It includes:
# - WINDOW_WIDTH: The width of the window or screen.
# - WINDOW_HEIGHT: The height of the window or screen.
# - PADS_POOL: Padding settings for layout management.
PADS_CONFIGS = (WINDOW_WIDTH, WINDOW_HEIGHT, PADS_POOL)