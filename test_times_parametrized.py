import pytest
from times import time_range, compute_overlap_time


@pytest.mark.parametrize("range1_start,range1_end,range1_intervals,range2_start,range2_end,range2_intervals,expected_empty", [
    # Test case 1: Non-overlapping time ranges
    ("2010-01-12 10:00:00", "2010-01-12 11:00:00", 1, 
     "2010-01-12 12:00:00", "2010-01-12 13:00:00", 1, True),
    
    # Test case 2: Multiple intervals with overlap
    ("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2,
     "2010-01-12 10:30:00", "2010-01-12 11:30:00", 3, False),
    
    # Test case 3: Adjacent time ranges
    ("2010-01-12 10:00:00", "2010-01-12 11:00:00", 1,
     "2010-01-12 11:00:00", "2010-01-12 12:00:00", 1, True),
    
    # Test case 4: Partial overlap
    ("2010-01-12 10:00:00", "2010-01-12 12:00:00", 1,
     "2010-01-12 11:00:00", "2010-01-12 13:00:00", 1, False),
    
    # Test case 5: Complete overlap
    ("2010-01-12 10:00:00", "2010-01-12 12:00:00", 1,
     "2010-01-12 09:00:00", "2010-01-12 13:00:00", 1, False),
])
def test_time_range_overlap(range1_start, range1_end, range1_intervals, 
                          range2_start, range2_end, range2_intervals, expected_empty):
    """Test time range overlap calculation with various scenarios"""
    range1 = time_range(range1_start, range1_end, range1_intervals)
    range2 = time_range(range2_start, range2_end, range2_intervals)
    
    overlap = compute_overlap_time(range1, range2)
    
    if expected_empty:
        assert overlap == []
    else:
        assert len(overlap) > 0
        # Verify overlap format
        for start, end in overlap:
            assert isinstance(start, str)
            assert isinstance(end, str)
            assert len(start) == 19  # "YYYY-MM-DD HH:MM:SS"
            assert len(end) == 19


@pytest.mark.parametrize("start_time,end_time,intervals,gap,should_raise", [
    # Valid cases
    ("2010-01-12 10:00:00", "2010-01-12 12:00:00", 1, 0, False),
    ("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60, False),
    
    # Invalid cases - backwards time
    ("2010-01-12 12:00:00", "2010-01-12 10:00:00", 1, 0, True),
    ("2010-01-12 10:00:00", "2010-01-12 10:00:00", 1, 0, True),
])
def test_time_range_validation(start_time, end_time, intervals, gap, should_raise):
    """Test time range input validation"""
    if should_raise:
        with pytest.raises(ValueError, match="End time must be after start time"):
            time_range(start_time, end_time, intervals, gap)
    else:
        result = time_range(start_time, end_time, intervals, gap)
        assert isinstance(result, list)
        assert len(result) == intervals
