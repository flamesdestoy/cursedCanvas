import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import MagicMock, patch

from console_wind import ConsoleScreen
from console_wind import Cursor

class TestConsoleScreen(unittest.TestCase):

    def setUp(self):
        # Create mock SubScreen instances
        self.mock_sub_screen1 = MagicMock()
        self.mock_sub_screen2 = MagicMock()
        
        # Mock the front buffer's clear method
        self.mock_sub_screen1.front_buffer.clear = MagicMock()
        self.mock_sub_screen2.front_buffer.clear = MagicMock()
        
        # Create a ConsoleScreen instance with mocked SubScreens
        self.console_screen = ConsoleScreen(
            inner_screens=[self.mock_sub_screen1, self.mock_sub_screen2],
            width=80,
            height=25,
            theme="dark"
        )

    def test_initialization(self):
        self.assertEqual(self.console_screen.width, 80)
        self.assertEqual(self.console_screen.height, 25)
        self.assertEqual(self.console_screen.theme, "dark")
        self.assertEqual(len(self.console_screen.sub_screens), 2)
        self.assertIsInstance(self.console_screen.cursor, Cursor)

    def test_str_method(self):
        expected_str = (
            "\nConsole window: \nwidth: 80 \nheight: 25"
            "\npad 0: <MagicMock id='...'>"
            "\npad 1: <MagicMock id='...'>"
        )
        self.assertIn("Console window:", str(self.console_screen))
        self.assertIn("width: 80", str(self.console_screen))
        self.assertIn("height: 25", str(self.console_screen))
        self.assertIn("pad 0:", str(self.console_screen))
        self.assertIn("pad 1:", str(self.console_screen))

    def test_clear(self):
        self.console_screen.clear()
        self.mock_sub_screen1.front_buffer.clear.assert_called_once()
        self.mock_sub_screen2.front_buffer.clear.assert_called_once()

    # @patch('console_wind.cursor.Cursor', autospec=True)
    # def test_cursor_initialization(self, MockCursor):
    #     self.assertIsInstance(self.console_screen.cursor, MockCursor)
    #     MockCursor.assert_called_once()

if __name__ == '__main__':
    unittest.main()
