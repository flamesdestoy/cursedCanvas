"""
Module: cmd_window_manager

This module defines the CmdWindowManager class, which is responsible for managing interactions
with the Command Prompt window. It includes functionality for creating and executing batch files,
retrieving the Command Prompt window size, clearing the screen, and managing command outputs.
"""

import subprocess
import threading
import time
import re
import os

class CommandManager:
    """
    A class to manage Command Prompt operations such as opening a Command Prompt window,
    executing batch files, retrieving window dimensions, and handling file operations.

    Attributes:
    -----------
    delay : float
        The time in seconds to wait for batch file execution.
    cmd_opening_delay : int
        The time in seconds to wait after opening the Command Prompt window before executing the batch file.
    batch_file_name : str
        The name of the batch file to be created.
    output_file_name : str
        The name of the file to store the Command Prompt dimensions output.
    batch_file_path : str
        The full path to the batch file.
    output_file_path : str
        The full path to the output file.
    """
    
    def __init__(
            self, batch_file_name='temp_batch.bat', 
            output_file_name='temp_mode_con.txt', wait_time=2.75
        ):
        """
        Initializes the CommandManager with specified file names and delay.

        Parameters:
        -----------
        batch_file_name : str, optional
            The name of the batch file (default is 'temp_batch.bat').
        output_file_name : str, optional
            The name of the output file (default is 'temp_mode_con.txt').
        wait_time : float, optional
            The time in seconds to wait for batch file execution (default is 2.75 seconds).
        """
        self.delay = wait_time
        self.cmd_opening_delay = 4
        self.batch_file_name = batch_file_name
        self.output_file_name = output_file_name
        self.batch_file_path = os.path.join(os.path.dirname(__file__), self.batch_file_name)
        self.output_file_path = os.path.join(os.path.dirname(__file__), self.output_file_name)
    
    def _create_batch_file(self):
        """
        Creates a batch file that executes the `mode con` command to output the Command Prompt dimensions.

        The batch file is saved to `self.batch_file_path` and includes a delay to ensure the Command Prompt window
        remains open long enough for execution.
        """
        batch_commands = f'''
        @echo off
        echo Executing mode con command... > "%~dp0{self.output_file_name}"
        mode con >> "%~dp0{self.output_file_name}"
        exit
        '''
        with open(self.batch_file_path, 'w') as file:
            file.write(batch_commands)
        time.sleep(self.delay - 1.5)
        # print(f"Batch file created at: {self.batch_file_path}")
        
    def _run_batch_file(self, title):
        """
        Opens a Command Prompt window with a specified title and executes the batch file.

        Parameters:
        -----------
        title : str
            The title to assign to the Command Prompt window.

        Notes:
        ------
        This method uses `subprocess.run` to start the Command Prompt with a `timeout` command to keep it open
        long enough to execute the batch file.
        """
        command = f'start cmd /k "title {title} & timeout /t {self.cmd_opening_delay + 1} & \"{self.batch_file_path}\""'
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error opening Command Prompt window with title '{title}': {e}")
    
    def close_opened_window(self, title):
        """
        Closes the Command Prompt window with the specified title.

        Parameters:
        -----------
        title : str
            The title of the Command Prompt window to close.

        Notes:
        ------
        This method uses `taskkill` to forcibly close the window.
        """
        try:
            command = f'taskkill /FI "WINDOWTITLE eq {title}" /F'
            
            subprocess.run(command, shell=True)
            print(f"Closed Command Prompt window with title: {title}")
        except Exception as e:
            print(f"Error closing Command Prompt window with title '{title}': {e}")
    
    def run_script(self, title, script_path):
        """
        Opens a Command Prompt window, assigns a title, and runs a specified Python script.

        Parameters:
        -----------
        title : str
            The title to assign to the Command Prompt window.
        script_path : str
            The path to the Python script to execute.

        Notes:
        ------
        This method uses `subprocess.run` to start the Command Prompt and execute the Python script.
        """
        command = f'start cmd /k "title {title} & python {script_path}"'
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error occurred when opening script at path '{script_path}': {e}")

    def _wait_for_batch_execution(self):
        """
        Waits for a specified delay to ensure that the batch file execution completes.

        This method uses `time.sleep` to pause execution for the duration specified by `self.delay`.
        """
        time.sleep(self.delay)

    def _read_and_parse_output(self):
        """
        Reads the output file generated by the batch file and extracts the dimensions of the Command Prompt window.

        Returns:
        --------
        tuple of (int, int) or (None, None)
            A tuple containing the width (columns) and height (lines) of the Command Prompt window.
            Returns (None, None) if the dimensions cannot be determined.

        Notes:
        ------
        This method uses a regular expression to parse the dimensions from the output file. The expected format is:
        "Lines: <number> Columns: <number>"
        """
        try:
            with open(self.output_file_path, 'r') as file:
                content = file.read()
                # print("Output file content:")
                # print(content)  # Debugging output

            # Adjusted regular expression based on actual output format
            match = re.search(r'Lines:\s+(\d+)\s+Columns:\s+(\d+)', content)
            if match:
                lines, cols = map(int, match.groups())
                return cols, lines
            else:
                print("Content format does not match expected pattern.")
                return None, None
        except FileNotFoundError:
            print(f"Output file {self.output_file_path} does not exist.")
            return None, None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None, None

    def _clear_screen(self):
        """
        Clears the Command Prompt screen.

        Notes:
        ------
        This method uses the `cls` command to clear the screen.
        """
        try:
            subprocess.call('cls', shell=True)
        except Exception as e:
            print(f"Error clearing Command Prompt screen: {e}")

    def _delete_file(self, file_path):
        """
        Deletes the specified file.

        Parameters:
        -----------
        file_path : str
            The path to the file to delete.

        Notes:
        ------
        This method checks if the file exists before attempting deletion.
        """
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                # print(f"File {file_path} deleted.")
            else:
                print(f"File {file_path} does not exist.")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    def _delete_created_files(self):
        """
        Deletes the batch file and output file created during the get_cmd_size operation.

        This method is intended to be run in a separate thread to perform file deletion without blocking
        the main thread of the get_cmd_size method.
        """
        try:
            self._delete_file(self.batch_file_path)
            self._delete_file(self.output_file_path)
        except Exception as e:
            print(f"Error deleting files: {e}")

    def get_cmd_size(self, title):
        """
        Opens a Command Prompt window, executes a batch file to retrieve the window dimensions, and deletes temporary files.

        The method performs the following steps:
        1. Creates a batch file to retrieve the dimensions of the Command Prompt window.
        2. Opens a Command Prompt window with a specified title and executes the batch file.
        3. Waits for the batch file to complete execution.
        4. Reads and parses the dimensions from the output file.
        5. Starts a background thread to delete temporary files (batch file and output file).
        6. Returns the width and height of the Command Prompt window.

        Parameters:
        -----------
        title : str
            The title to assign to the Command Prompt window.

        Returns:
        --------
        tuple of (int, int) or (None, None)
            A tuple containing the width and height of the Command Prompt window in columns and lines respectively.
            Returns (None, None) if the dimensions cannot be determined.

        Exceptions:
        -----------
        Raises:
            Exception: If any error occurs during the operation, an error message is printed, and (None, None) is returned.

        Notes:
        ------
        - The method assumes that the Command Prompt window will remain open long enough to complete the execution of the batch file.
        - The batch file includes a `timeout` command to ensure that the Command Prompt window remains open after execution.
        - A separate thread is used to delete temporary files to avoid blocking the main thread, allowing the dimension retrieval to complete first.
        """
        try:
            self._create_batch_file()  # Creating a batch file
            self._run_batch_file(title)  # Executing the batch file to get con
            self._wait_for_batch_execution()  # Sleeps for some delay time
            width, height = self._read_and_parse_output()  # Get the width & height from file

            if width is not None and height is not None:
                # Start a thread to delete the files
                deletion_thread = threading.Thread(
                    target=self._delete_created_files
                )
                deletion_thread.start()  # Start the thread for deletion
                return width, height
            else:
                print("Unable to determine command prompt size.")
                return None, None
        except Exception as e:
            print(f"Error during update operation: {e}")
            return None, None
