"""
This module provides an interface to open the console window in any 
platform adhering to the open/closed principle to let the framework
run in multiple platforms.

Classes:
    ConsolePopper: Class which imposes the popen_window method to start
    up the window.
"""

from abc import ABC, abstractmethod

class ConsolePopper(ABC):
    """
    An interface to abstractly use the popen_window method.
    """
    # Console window opening method
    @abstractmethod
    def popen_window(self, 
                     title: str, 
                     script_path="", 
                     use_terminal=False
                    ) -> tuple[int, int]:
        """ Opens the console window, running on it a script. """
        pass
