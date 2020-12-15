import times

def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_no_overlap():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = []
    assert result == expected   

def test_multiple_overlap():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900)
    short = times.time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2 , 120)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:40:00', '2010-01-12 10:50:00'), ('2010-01-12 11:05:00', '2010-01-12 11:20:00')]
    assert result == expected    

def test_touching():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00")
    short = times.time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
    result = times.compute_overlap_time(large, short)
    expected = []
    assert result == expected    