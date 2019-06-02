import pytest

def fizzbuzz(value):
	if value % 15 == 0:
		return "FizzBuzz"
	if value % 3 == 0:
		return "Fizz"
	if value % 5 == 0:
		return "Buzz"
	return str(value)


def test_fizzbuzz_return( value=1, expecdtedRetVal='1'):
	retVal=fizzbuzz(value)
	assert retVal == expecdtedRetVal

def test_returns1with1PassedIn():
	test_fizzbuzz_return(1,"1")


def test_returns2with2PassedIn():
	test_fizzbuzz_return(2,"2")

def test_returnsFizzwith3PassedIn():
	test_fizzbuzz_return(3,"Fizz")

def test_returnsBuzzwith5PassedIn():
	test_fizzbuzz_return(5,"Buzz")

def test_returnsFizzwith6PassedIn():
	test_fizzbuzz_return(6,"Fizz")

def test_returnsBuzzwith10PassedIn():
	test_fizzbuzz_return(10,"Buzz")

def test_returnsFizzBuzzwith15PassedIn():
	test_fizzbuzz_return(15,"FizzBuzz")

