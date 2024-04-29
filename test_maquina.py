import pytest
from palindromos import palindromos as dtm

@pytest.mark.parametrize("capicua", [
    "aa",
    "bb",
    "abba",
    "abaaba",
    "aabbaa",
    "aabbbbaa",
    "ababaababa",
])
def test_acepta(capicua):
    assert dtm.accepts_input(capicua)

@pytest.mark.parametrize("no_capicua", [
    "a",
    "b",
    "ab",
    "ba",
    "ababababa"
])
def test_rechaaza(no_capicua):
    assert not dtm.accepts_input(no_capicua)
