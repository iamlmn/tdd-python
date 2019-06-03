# Test Driven Development in Python

`What is TDD?`

> A process where the developer takes personal responsibiltiy for the quality of their code.
> Unit tests are written before the productin code.

#### Benefits?

1. Gives confidence on your code.
2. Gives you immediate feedback
3. Documents what the code is doing.
4. Drives good object oriented design.

#### Workflo

__Red__ > __Green__ > __Refactor__


###### Uncle BOB's 3 Laws of TDD.

* You may not rote any producton doce until you have written a failing unit test. 

* You may not write more of a unit test than is sufficient to fail and not compiling is failing.

* You may not write more production code than is sufficient to pass the current failing unit test.

---

##### Unit testing?

Why do we need unit test?

 * Software bugs hurt the business
 * Software testing catches the bugs before they get to the field.
 * Need several levels of safety nets.


##### Levels of Testing

* Unit Testing - Testing at the function level

* Component Testing - Testing is at the library compiled binary level

* System Testing - Tests the externam interfaces of a system which is a collection of sub-systems.

* Perfomance Testing - Testing done at sub-system and system levels to verify timing and resource usages are acceptable.



#### Unit testing spevifics 

* Tests induvudual fucntions
* A test should be written for each test case for a function (Positve & negative cases).
* Groups of tests can be combined into test suites for better organization. Executes in the development env and not in prod.
*  Should be automated.
* unit tests should run fast.


#### Virtual Envs for Testing.

Virtual envs solve the dependency issue by creating isolated python environments thst can be customized per project
Virtual Envs are directoris containing links ot the system's python install and providing sub-directories for installing additional python packages in that particular VE.
The PATH env variable is updated to point to the virtual env when that ve is activated.

* ``` pip install virtualenv ```
* Create a venv ->  ``` virtualenv<Name ```
* Activate the venv by sorucing the activate script in bin -> ``` soruce./<Name>/bin/activate ```
* Deactivate -> ``` deactivate ```
* Delete venv by deleting the directory.

or venv in python3 (comes by default in python>3) except for creating venv -> ``` python3 -m venv <Name> ```

***

### What is PyTest?

* PyTest is a python unit test frameork.
* It provides ability to provide Test,TestModules,Test Fixtures.
* Uses built in assert statement.
* Command line paramets to view which tests are executed and in what order!

##### Tests
> Tests are python function with "test" at the begining of the function name.
Tests does standard verification of values using assert method.

##### Test Discovery

> PyTest will automatically discover tests when we follow some standard conventions.
Test functions should have tests in the beginning of the function name.
Test Classes should have "Test" in the beginning of the class and name and SHOULD NOT have __init__ method.
File name should start with test_example.py or end with example_test.py  
 


### XUnit setup and teardown.

> One key feature of all unit test frameworks is providing the ability to execute setup code before and after the tests. Pytest provides this capability with both XUnit
style setup/teardown functions and with Pytest fixtures.
... The XUnit style setup and teardown functions allow you to execute code before and after: Test modules <click>, Test Functions <click>, Test Classes <click>, and Test
Methods in Test Classes.
... Using these setup and teardown functions can help reduce code duplication by letting you specify setup and teardown code once at each of the different levels as
necessary rather than repeating the code in each individual unit test. 

``` python3 -m pytest -v -s test_Xunit.py```


### TEST FIXTURES

* Test fixtures allows to re-use setup and teardown code accross the tests.
* The python.fixture decorator is applied to functions that are decorators.
* Induvidual test cases can specify which fixtures they want executed.
* The autouse parameter can be set to true to automatically execute a fixture before each tests.

---

## Pytest & cmd 
> By default Pytest runs all tests that it finds in the current working directory and sub-directory using the naming conventions for automatic test discovery.
- There are several pytest command line arguments that can be specified to try and be more selective about which tests will be executed.
- You can simply pass in the module name to execute only the unit tests in one particular module.
- You can also simply pass in a directory path to have pytest run only the tests in that directory.
- You can use the “-k” option to specify an evaluation string based on keywords such as: module name, class name, and function name.
- You can use the “-m” option to specify that any tests that have a “pytest.mark” decorator that matches the specified expression string will be executed.

Here are some additional command line arguments that can be very useful.
- The -v option specifies that verbose output from pytest should be enabled.
- The -q option specifies the opposite. It specifies that the tests should be run quietly (or minimal output). This can be helpful from a performance perspective when
you’re running 100’s or 1000’s of tests.
- The -s option specifies that PyTest should NOT capture the console output.
- The —ignore option allows you to specify a path that should be ignore during test discovery.
- The —maxfail option specifies that PyTest should stop after N number of test failures.


***

### Test Doubles

##### Almosy depends on other parts of the system which are not easy to replicate in unit test environment or would make tests slow. In such scenarios we use Test doubles.

	* Dummy - Objects can be passed around as necessary but do not have any type of test implementation and should be never used.
	* Fake - These objects generally have a simplified functional implementation of a particular interface that is adequate for testing not for production.
	* Stub - These objects provide implementation with canned answers that are suitable for the test.
	* Spies - These objects provide implementations that record the values that were passed in so they can be tested.
	* Mocks- These objects are preprogrammed to expect specific calls and parameters and can throw exceptions when necessary.

unittest.mock - Python mock library
 - pip install mock , built-in for python > 3.3
 - MAgicMock & Monekypatch






