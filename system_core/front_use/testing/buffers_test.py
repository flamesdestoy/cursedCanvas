import unittest
from dataclasses import dataclass
import sys
import os

# Add the parent directory of 'console_wind' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from console_wind.buffers.abstract_buffer import Buffer
from console_wind.buffers import FrontBuffer, BackBuffer
from console_wind.utils.buffers_utils import create_grid
from console_wind.data_configs.buffers_configs import (
    DEFAULT_GRID_CHAR, MAX_BACK_BUFFER_WIDTH,
    ADJUSTMENT_RANGE_TOP, MAX_BACK_BUFFER_HEIGHT
)
class TestBuffer(unittest.TestCase):

    class ConcreteBuffer(Buffer):
        def init_buffer(self):
            self._grid = create_grid(self._width, self._height, self.grid_char)

    def setUp(self):
        self.buffer = self.ConcreteBuffer(10, 10)

    def test_initialization(self):
        self.assertEqual(self.buffer.width, 10)
        self.assertEqual(self.buffer.height, 10)
        self.assertEqual(len(self.buffer.grid), 10)
        self.assertEqual(len(self.buffer.grid[0]), 10)

    def test_access_character(self):
        self.assertEqual(self.buffer.access_character(0, 0), DEFAULT_GRID_CHAR)

    def test_modify_character(self):
        self.buffer.modify_character(0, 0, 'A')
        self.assertEqual(self.buffer.access_character(0, 0), 'A')

    def test_remove_character(self):
        self.buffer.modify_character(0, 0, 'A')
        self.buffer.delete_character(0, 0)
        self.assertNotEqual(self.buffer.access_character(0, 0), 'A')

    def test_clear(self):
        self.buffer.modify_character(0, 0, 'A')
        self.buffer.clear()
        self.assertEqual(self.buffer.access_character(0, 0), DEFAULT_GRID_CHAR)


class TestBackBuffer(unittest.TestCase):

    def setUp(self):
        self.back_buffer_small = BackBuffer(5, 5)
        self.back_buffer_large = BackBuffer(50, 50)

    def test_init_buffer_small(self):
        self.back_buffer_small.init_buffer()
        self.assertEqual(len(self.back_buffer_small.grid), 5)
        self.assertEqual(len(self.back_buffer_small.grid[0]), 5)

    def test_init_buffer_large(self):
        self.back_buffer_large.init_buffer()
        self.assertEqual(len(self.back_buffer_large.grid), MAX_BACK_BUFFER_HEIGHT)
        self.assertEqual(len(self.back_buffer_large.grid[0]), MAX_BACK_BUFFER_WIDTH)


class TestFrontBuffer(unittest.TestCase):

    def setUp(self):
        self.front_buffer = FrontBuffer(10, 10)

    def test_init_buffer(self):
        self.front_buffer.init_buffer()
        self.assertEqual(len(self.front_buffer.grid), 10)
        self.assertEqual(len(self.front_buffer.grid[0]), 10)


if __name__ == '__main__':
    unittest.main()
