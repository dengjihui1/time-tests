import unittest
from times import time_range, compute_overlap_time


class TestTimeRanges(unittest.TestCase):
    
    def test_non_overlapping_time_ranges(self):
        """Test non-overlapping time ranges"""
        range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
        range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
        
        overlap = compute_overlap_time(range1, range2)
        self.assertEqual(overlap, [])

    def test_multiple_intervals_in_each_range(self):
        """Test ranges with multiple intervals"""
        range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
        range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 3)
        
        overlap = compute_overlap_time(range1, range2)
        self.assertGreater(len(overlap), 0)
        
        for start, end in overlap:
            self.assertIsInstance(start, str)
            self.assertIsInstance(end, str)
            self.assertEqual(len(start), 19)
            self.assertEqual(len(end), 19)

    def test_adjacent_time_ranges(self):
        """Test adjacent time ranges"""
        range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
        range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
        
        overlap = compute_overlap_time(range1, range2)
        self.assertEqual(overlap, [])


if __name__ == "__main__":
    unittest.main()
