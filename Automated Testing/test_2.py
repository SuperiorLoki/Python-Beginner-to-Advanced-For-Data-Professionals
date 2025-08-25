import pytest

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def test_multiply():
    assert multiply(2,5) == 10
    assert multiply(4,4) == 16

def test_divide():
    assert divide(4,2) == 2
    assert divide(20, 4) == 5
    #To test for a value error that should be raised
    with pytest.raises(ValueError):
        assert divide(5,0)