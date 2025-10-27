from times import compute_overlap_time, time_range
import pytest

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    expected = []
    assert compute_overlap_time(range1, range2) == expected

def test_multiple_intervals():
    range1 = time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 3, 30)
    range2 = time_range("2010-01-12 10:15:00", "2010-01-12 11:45:00", 3, 20)
    result = compute_overlap_time(range1, range2)
    
    assert len(result) > 0
    
    assert result[0][0] < result[0][1]

def test_touching_endpoints():
    range1 = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00")
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    expected = [] 
    assert compute_overlap_time(range1, range2) == expected

def test_time_range_backwards_raises():
    with pytest.raises(ValueError, match="before start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 11:00:00")