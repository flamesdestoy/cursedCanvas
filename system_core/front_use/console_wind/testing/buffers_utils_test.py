import unittest
import sys
import os

# Add the parent directory of 'console_wind' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from console_wind.utils.buffers_utils import create_grid, validate_grid

class TestGridFunctions(unittest.TestCase):
    def test_create_grid(self):
        """Test the create_grid function."""
        grid = create_grid(4, 3, 'x')
        expected_grid = [
            ['x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x']
        ]
        self.assertEqual(grid, expected_grid)

    def test_create_grid_empty(self):
        """Test creating an empty grid."""
        grid = create_grid(0, 0, 'x')
        expected_grid = []
        self.assertEqual(grid, expected_grid)

    def test_validate_grid_valid(self):
        """Test validation of a valid rectangular grid."""
        grid = [
            ['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['x', 'x', 'x']
        ]
        self.assertTrue(validate_grid(grid))

    def test_validate_grid_invalid_row_length(self):
        """Test validation of an invalid grid with varying row lengths."""
        grid = [
            ['x', 'x', 'x'],
            ['x', 'x'],
            ['x', 'x', 'x']
        ]
        self.assertFalse(validate_grid(grid))

    def test_validate_grid_empty(self):
        """Test validation of an empty grid."""
        grid = []
        self.assertTrue(validate_grid(grid))

    def test_validate_grid_one_row(self):
        """Test validation of a grid with one row."""
        grid = [['x', 'x', 'x']]
        self.assertTrue(validate_grid(grid))

    def test_validate_grid_one_column(self):
        """Test validation of a grid with one column."""
        grid = [['x'], ['x'], ['x']]
        self.assertTrue(validate_grid(grid))

    def test_validate_grid_mixed_characters(self):
        """Test validation of a grid with mixed characters."""
        grid = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        self.assertTrue(validate_grid(grid))

if __name__ == '__main__':
    unittest.main()
