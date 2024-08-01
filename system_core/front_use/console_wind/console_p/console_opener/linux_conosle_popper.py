"""
This module provides a concrete class realizing the ConsolePopper 
interface for opening the console window using polymorphism.

Classes:
    LinuxConsolePopper: Class implements the interface 
    ConsolePopper.
"""
from os import get_terminal_size
from dataclasses import dataclass
import subprocess

from .console_popper_interface import ConsolePopper
from ..window_core.default_init_params import (
    CMD_OPENING_WIDTH_LIMIT,
    CMD_OPENING_HEIGHT_LIMIT
)

@dataclass
class LinuxConsolePopper(ConsolePopper):
    """ 
    Class to Implement the ConsolePopper interface. 

    Methods:
        popen_window: Opens the window taking some parameters.
    """
    # properties
    
    # methods
    def popen_window(self, 
                     title: str, 
                     script_path="", 
                     use_terminal=False
                    ) -> tuple[int, int]:
        """
        Opens up the console window and runs the program.

        Args:
            title (str): write the screen title
            width (int): specializing screen width
            height (int): specializing screen height
        """

        # Run on cmd if authorization given else run on emulator
        if use_terminal:
            # Open cmd command
            command = f'''
            gnome-terminal 
            --geometry={terminal_width}x{terminal_height} 
            --title="{title}" 
            -- bash -c "python3 {script_path}; 
            exec bash"'''
            
            subprocess.run(command, shell=True)  # runs the command
        else:  # Run on VsCode
            size = get_terminal_size()  # Get terminal dimensions
            terminal_width = size.columns
            terminal_height = size.lines

        return terminal_height, terminal_width  # Gives the terminal window size
    