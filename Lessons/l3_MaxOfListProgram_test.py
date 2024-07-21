from Lessons.l3_MaxOfListProgram import *


def test_max_list():
    list_one = [3, 6, 2, 1, 8, 4, 4, 2, 7]
    list_two = [30, 16, 4, 45, 27, 84]
    list_three = [-10, -4, -3, -2]
    assert max_list(list_one) == 8
    assert max_list(list_two) == 84
    assert max_list(list_three) == -2