import pytest

from pythontest.Baseclass import Baseclass


@pytest.mark.xfail


def test_program1(setup):
    print("Hi")

def test_addProgram1():
    print("Tiya")

#@pytest.mark.usefixtures("browesers")
#class TestExample3(Baseclass):

#    def test_browesers(self, browesers):
 #       log = self.getlogger()
  #      log.info(browesers[1])
   #     log.info(browesers[0])

