from Line import Line


def test_init_line_regular():
    line = Line([5, 5], [10, 10])
    assert(line._start == [5, 5])
    assert(line._end == [10, 10])

