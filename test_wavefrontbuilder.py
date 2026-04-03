# test_wavefrontbuilder.py
"""
Tests for WaveFrontBuilder module.
"""

import unittest
from wavefrontbuilder import WaveFrontBuilder

class TestWaveFrontBuilder(unittest.TestCase):
    """Test cases for WaveFrontBuilder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WaveFrontBuilder()
        self.assertIsInstance(instance, WaveFrontBuilder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WaveFrontBuilder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
