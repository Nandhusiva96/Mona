import pytest


@pytest.mark.usefixtures("setup")
class Testexamples:

    def test_fixturedemo(self):
        print("I will execute steps in fixture method")

    def test_fixturedemo1(self):
        print("I will execute steps in fixture1 method")

    def test_fixturedemo2(self):
        print("I will execute steps in fixture2 method")

    def test_fixturedemo3(self):
        print("I will execute steps in fixture3 method")

    def test_fixturedemo4(self):
        print("I will execute steps in fixture4 method")