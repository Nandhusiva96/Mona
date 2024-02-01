import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")

    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Siva", "Mohanapriya", "Tiyashna"]

@pytest.fixture(params=[("chrome","siva", "nandhu", "Tiya"), ("Firefox", "Nandhu"), ("IE", "Tiya")])
def browesers(request):
    return request.param
