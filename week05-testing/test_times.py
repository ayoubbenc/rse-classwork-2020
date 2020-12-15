import times
import pytest

def test_given_input():
    t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    t2 = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(t1, t2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_no_overlap():
    t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    t2 = times.time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = times.compute_overlap_time(t1, t2)
    expected = []
    assert result == expected   

def test_multiple_overlap():
    t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900)
    t2 = times.time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2 , 120)
    result = times.compute_overlap_time(t1, t2)
    expected = [('2010-01-12 10:40:00', '2010-01-12 10:50:00'), ('2010-01-12 11:05:00', '2010-01-12 11:20:00')]
    assert result == expected    

def test_touching():
    t1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00")
    t2 = times.time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
    result = times.compute_overlap_time(t1, t2)
    expected = []
    assert result == expected    

def test_negative():
    with pytest.raises(ValueError) as e:
        times.time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
    assert e.match('The end of the time range has to come strictly after its start.')