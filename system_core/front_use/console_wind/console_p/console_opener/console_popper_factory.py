"""
Factory module for creating platform-specific console popper instances.

This module provides the `ConsolePopperFactory` class, which is responsible for 
determining the current platform and instantiating the appropriate subclass 
of the `ConsolePopper` interface. This allows the application to open console windows 
in a platform-independent manner.

Classes:
    ConsolePopperFactory: A factory class for creating platform-specific console poppers.
"""
import platform

from .console_popper_interface import ConsolePopper
from .windows_conosle_popper import WindowsConsolePopper
from .linux_conosle_popper import LinuxConsolePopper
from .macOs_conosle_popper import MacOsConsolePopper

class ConsolePopperFactory:
    """
    A factory class responsible for creating instances of platform-specific console poppers.

    This class contains a static method `create_console_popper` that checks the current 
    operating system and returns an appropriate instance of a class implementing the 
    `ConsolePopper` interface.

    Methods:
        create_console_popper(): Determines the platform and returns a corresponding 
                                 instance of ConsolePopper.
    """
    @staticmethod
    def create_console_popper() -> ConsolePopper:
        """
        Creates and returns an instance of a platform-specific ConsolePopper.

        This method uses the `platform.system()` function to determine the current 
        operating system. Based on the detected platform, it returns an instance of the 
        appropriate subclass of `ConsolePopper`.

        Returns:
            ConsolePopper: An instance of a class implementing the `ConsolePopper` interface, 
                           specific to the current platform.

        Raises:
            NotImplementedError: If the current platform is not supported.
        """
        current_platform = platform.system()
        if current_platform == "Windows":  # Windows
            return WindowsConsolePopper()
        elif current_platform == "Linux":  # Linux
            return LinuxConsolePopper()
        elif current_platform == "Darwin":  # MacOS
            return MacOsConsolePopper()
        else:
            raise NotImplementedError(f"ConsolePopper not implemented for platform: {current_platform}")
