"""
Unit tests using pytest
"""
import app

def test_addition():
    assert 4 == app.add(2, 2)

def test_subtraction():
    assert 2 == app.subtract(4, 2)
