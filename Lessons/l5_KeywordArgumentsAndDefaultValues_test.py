import inspect
import io
from unittest.mock import patch

import pytest

from l5_KeywordArgumentsAndDefaultValues import *


def test_print_list_function_exists():
    function_name = "print_list"
    assert function_name in globals(), (f"The function '{function_name}' is not defined. Make sure you've created a "
                                        f"function called 'print_list'.")


def test_print_list_arguments():
    argspec = inspect.getfullargspec(print_list)
    arguments = argspec.args[:len(argspec.args) - len(argspec.defaults)] if argspec.defaults else argspec.args
    assert len(
        arguments) == 1, ("The 'print_list' function should take exactly one positional argument (the list to print). "
                          "Check your function definition.")

    keyword_arguments = argspec.args[-len(argspec.defaults):] if argspec.defaults else []
    assert "multiple" in keyword_arguments, ("The 'print_list' function should have a keyword argument called "
                                             "'multiple'. Make sure you've defined it in your function.")


@pytest.mark.parametrize("input_list, multiple, expected_output", [
    ([4, 3, 2, 1], None, "4\n3\n2\n1\n"),
    ([2, 3, 6, 4], 2, "4\n6\n12\n8\n"),
    ([2, 3, 6, 4], 3, "6\n9\n18\n12\n"),
    ([2, 3, 6, 4], 5, "10\n15\n30\n20\n")
])
def test_print_list_output(input_list, multiple, expected_output):
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        if multiple is None:
            print_list()
        else:
            print_list()
        actual_output = fake_out.getvalue()
        assert actual_output == expected_output, f"Expected output:\n{expected_output}\nBut got:\n{actual_output}\nCheck your function's logic, especially how it handles the 'multiple' parameter."
