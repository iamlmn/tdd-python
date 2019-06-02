import pytest
class TestClass:

	@classmethod
	def setup_class(cls):
		print("Setup Class")

	@classmethod
	def teardown_class(cls):
		print("TearDown Class")


	def setup_method(self,method):
		if method == self.test1 :
			print("\nSetting up test1")
		elif method == self.test2 :
			print("\n Setting up test2")
		else:
			print("\n Setting up unknown test!")


	def teardown_method(self,method):
		if method == self.test1 :
			print("\n Tearing down test1")
		elif method == self.test2 :
			print("\n Tearing down test2")
		else:
			print("\n Tearing down unknown test!")


	def test1(self):
		print("Executing Test1")
		assert True


	def test2(self):
		print("Executing Test2")
		assert True