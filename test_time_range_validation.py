import unittest
from times import time_range


class TestTimeRangeValidation(unittest.TestCase):
    
    def test_backwards_time_range_raises_error(self):
        """Test that backwards time range raises ValueError"""
        with self.assertRaises(ValueError) as context:
            time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        
        self.assertEqual(str(context.exception), "End time must be after start time")
    
    def test_equal_start_end_time_raises_error(self):
        """Test that equal start and end time raises ValueError"""
        with self.assertRaises(ValueError) as context:
            time_range("2010-01-12 10:00:00", "2010-01-12 10:00:00")
        
        self.assertEqual(str(context.exception), "End time must be after start time")
    
    def test_valid_time_range_works(self):
        """Test that valid time range works correctly"""
        result = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ("2010-01-12 10:00:00", "2010-01-12 12:00:00"))


if __name__ == "__main__":
    unittest.main()
