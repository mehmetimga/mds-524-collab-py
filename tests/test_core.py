from mehmetmga_py_524 import add_two


def test_add_two():
    assert add_two(1, 2) == 3
    assert add_two(-1, 1) == 0
    assert add_two(0, 0) == 0

