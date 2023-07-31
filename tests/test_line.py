from Line import Line


def test_init_line_regular():
    line = Line([5, 5], [10, 10])
    assert(line._start == [5, 5])
    assert(line._end == [10, 10])


def test_init_line_reversed():
    line = Line([10, 10], [5, 5])
    assert(line._start == [5, 5])
    assert(line._end == [10, 10])


def test_init_line_check_a():
    line = Line([5, 7], [10, 18])
    assert(line._a == (7 - 18)/(5 - 10))


def test_init_line_check_b():
    line = Line([5, 7], [10, 18])
    assert(line._b == (7 - (7 - 18)/(5 - 10)*5))
