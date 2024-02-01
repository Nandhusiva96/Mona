import pytest

from pythontest.Baseclass import Baseclass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(Baseclass):
    def test_EditData(self, dataLoad):
        log = self.getlogger()
        log.info(dataLoad[2])
        log.info(dataLoad[0])
        print(dataLoad[0])