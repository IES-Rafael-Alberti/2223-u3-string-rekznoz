from src.main2 import string_comlpeto
import pytest

def test_string_comlpeto():
    assert string_comlpeto("hola") == "hola"
    assert string_comlpeto("push") == "push"
    assert string_comlpeto("12345") == "12345"