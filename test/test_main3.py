from src.main3 import cuenta
import pytest

def test_cuenta():
    assert cuenta('platano', 'a') == 2
    assert cuenta('banana', 'z') == 0
    assert cuenta('', 'a') == 0