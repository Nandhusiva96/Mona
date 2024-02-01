import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_program2():
    a = "Tiya"
    assert a == "Sivanandhu", "This string is not matched"

def test_addprogram1():
    a=4
    b=6
    assert a+2 == 6, "Addition is not matched"


def test_addprogram1():
    a=4
    b=6
    assert a+2 == 6, "This is not matched"



