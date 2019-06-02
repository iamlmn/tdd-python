import pytest

@pytest.fixture()
def setup1():
	print("\n Setup 1")
	yield
	print("\n Teardown1")


@pytest.fixture()
def setup2(request):
	print("\n Setup 2")

	def teardown_a():
		print("\n Teardown A")
	def teardown_b():
		print("\n TearDown B")

	request.addfinalizer(teardown_a)
	request.addfinalizer(teardown_b)

def test1(setup1):
	print("Executing Test1")
	assert True
	
def test2(setup2):
	print("Executing Test2")
	assert True