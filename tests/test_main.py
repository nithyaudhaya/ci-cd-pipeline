from src.main import Maths

def test_add_function():
    assert Maths.add(2, 3) == 5
    assert Maths.add(0, 0) == 1
    assert Maths.add(5, 5) == 10

def test_subtarct_function():
    assert Maths.subtract(5, 3) == 2
    assert Maths.subtract(0, 0) == 0
    assert Maths.subtract(10, 5) == 5