# test_moralshield.py
"""
Tests for MoralShield module.
"""

import unittest
from moralshield import MoralShield

class TestMoralShield(unittest.TestCase):
    """Test cases for MoralShield class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MoralShield()
        self.assertIsInstance(instance, MoralShield)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MoralShield()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
