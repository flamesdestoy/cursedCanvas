import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import MagicMock

from console_wind.sub_screens.sub_screen import SubScreen

class TestSubScreen(unittest.TestCase):

    def setUp(self):
        # Mock FrontBuffer and BackBuffer classes
        self.front_buffer_mock = MagicMock()
        self.back_buffer_mock = MagicMock()

        # Mock the methods of FrontBuffer and BackBuffer
        self.front_buffer_mock.width = 10
        self.front_buffer_mock.height = 10
        self.front_buffer_mock.grid = [['x'] * 10 for _ in range(10)]
        self.front_buffer_mock.init_buffer = MagicMock()
        self.front_buffer_mock.clear = MagicMock()
        self.front_buffer_mock.display_grid = MagicMock()

        self.back_buffer_mock.width = 10
        self.back_buffer_mock.height = 10
        self.back_buffer_mock.grid = [['x'] * 10 for _ in range(10)]
        self.back_buffer_mock.init_buffer = MagicMock()

        # Create SubScreen instance with mocked buffers
        self.sub_screen = SubScreen(10, 10)
        self.sub_screen._front_buffer = self.front_buffer_mock
        self.sub_screen._back_buffer = self.back_buffer_mock

    def test_init_sub_screen(self):
        self.assertEqual(self.sub_screen.front_buffer, self.front_buffer_mock)
        self.assertEqual(self.sub_screen.back_buffer, self.back_buffer_mock)
        self.assertEqual(self.sub_screen._width, 10)
        self.assertEqual(self.sub_screen._height, 10)

    def test_clear(self):
        self.sub_screen.clear()
        self.front_buffer_mock.clear.assert_called_once()

    def test_swap_buffers(self):
        # Setup initial state
        self.sub_screen._front_buffer.grid = [['a'] * 10 for _ in range(10)]
        self.sub_screen._back_buffer.grid = [['b'] * 10 for _ in range(10)]

        # Call swap_buffers method
        self.sub_screen.swap_buffers()

        # Check if grids are swapped
        self.assertEqual(self.sub_screen._front_buffer.grid, [['b'] * 10 for _ in range(10)])
        self.assertEqual(self.sub_screen._back_buffer.grid, [['a'] * 10 for _ in range(10)])

    def test_display_content(self):
        self.sub_screen.display_content()
        self.front_buffer_mock.display_grid.assert_called_once()

if __name__ == '__main__':
    unittest.main()
