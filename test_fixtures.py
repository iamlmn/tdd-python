import pytest

#@pytest.fixture()
@pytest.fixture(autouse=True)
def setup():
	print("\n Setup")

def test1(setup):
	print("Executing test1")
	assert True

@pytest.mark.usefixtures("setup")
def test2():
	print("Executing Test2!")
	assert True

def test3():
	print("Executing Test3!")
	assert True