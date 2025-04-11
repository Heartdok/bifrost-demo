"""
Tests for the utils module.
"""
import unittest
import sys
import os

# Add the parent directory to the path so we can import the utils module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils


class TestUtils(unittest.TestCase):
    """Test cases for the utils module."""

    def test_calculate_sum(self):
        """Test the calculate_sum function."""
        # Test with positive numbers
        self.assertEqual(utils.calculate_sum(5, 3), 8)
        
        # Test with negative numbers
        self.assertEqual(utils.calculate_sum(-5, -3), -8)
        
        # Test with mixed numbers
        self.assertEqual(utils.calculate_sum(5, -3), 2)
        
        # Test with zero
        self.assertEqual(utils.calculate_sum(0, 0), 0)
        
        # Test with floating point numbers
        self.assertAlmostEqual(utils.calculate_sum(5.5, 3.3), 8.8)

    def test_multiply(self):
        """Test the multiply function."""
        # Test with positive numbers
        self.assertEqual(utils.multiply(5, 3), 15)
        
        # Test with negative numbers
        self.assertEqual(utils.multiply(-5, -3), 15)
        
        # Test with mixed numbers
        self.assertEqual(utils.multiply(5, -3), -15)
        
        # Test with zero
        self.assertEqual(utils.multiply(5, 0), 0)
        
        # Test with floating point numbers
        self.assertAlmostEqual(utils.multiply(5.5, 2), 11)


if __name__ == '__main__':
    unittest.main()
