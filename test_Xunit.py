

def setup_module(module):
	print("Setup Module")


def teardown_module(module):
	print("TearDown Module")


def setup_function(function):
	if function == test1 :
		print("\nSetting up test1")
	elif function == test2 :
		print("\n Setting up test2")
	else:
		print("\n Setting up unknown test!")


def teardown_function(function):
	if function == test1 :
		print("\n Tearing down test1")
	elif function == test2 :
		print("\n Tearing down test2")
	else:
		print("\n Tearing down unknown test!")


def test1():
	print("Executing Test1")
	assert True



def test2():
	print("Executing Test2")
	assert True