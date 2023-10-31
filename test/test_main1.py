from src.main1 import str_reverse
import pytest

def test_reverse_string():
    assert str_reverse("hola") == "a\nl\no\nh\n"
    assert str_reverse("12345") == "5\n4\n3\n2\n1\n"
    assert str_reverse("") == ""