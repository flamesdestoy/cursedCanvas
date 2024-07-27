import unittest
import sys
import os

# Add the parent directory of 'console_wind' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
DEFAULT_CURSOR_POSITION = (0, 0)
DEFAULT_CURSOR_VISIBILITY = True
# Your Cursor class should be imported here
from console_wind.cursor import Cursor

class TestCursor(unittest.TestCase):
    def setUp(self):
        """Create a Cursor instance for testing."""
        self.cursor = Cursor()

    def test_initial_values(self):
        """Test the initial values of cursor attributes."""
        self.assertEqual(self.cursor.cursor_position, DEFAULT_CURSOR_POSITION)
        self.assertEqual(self.cursor.cursor_visibility, DEFAULT_CURSOR_VISIBILITY)

    def test_set_cursor_position(self):
        """Test the cursor_position setter and getter."""
        new_position = (10, 20)
        self.cursor.cursor_position = new_position
        self.assertEqual(self.cursor.cursor_position, new_position)

    def test_set_cursor_visibility(self):
        """Test the cursor_visibility setter and getter."""
        new_visibility = False
        self.cursor.cursor_visibility = new_visibility
        self.assertEqual(self.cursor.cursor_visibility, new_visibility)

    def test_set_cursor_visibility_no_change(self):
        """Test that cursor_visibility is not changed if the value is the same."""
        original_visibility = self.cursor.cursor_visibility
        self.cursor.cursor_visibility = original_visibility
        self.assertEqual(self.cursor.cursor_visibility, original_visibility)

if __name__ == '__main__':
    unittest.main()
