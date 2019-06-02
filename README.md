### Test Driven Development in Python

What is TDD?

A process where the developer takes personal responsibiltiy for the quality of their code.
Unit tests are written before the productin code.

#### Benefits?

1 Gives confidence on your code.
2 Gives you immediate feedback
3 Documents what the code is doing.
4 Drives good object oriented design.

#### Workflo

RED -> GREEN -> Refactor


###### Uncle BOB's 3 Laws of TDD.

* You may not rote any producton doce until you have written a failing unit test. 

* You may not write more of a unit test than is sufficient to fail and not compiling is failing.

* You may not write more production code than is sufficient to pass the current failing unit test.


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

* pip install virtualenv
* Create a venv ->virtualenv<Name>
* Activate the venv by sorucing the activate script in bin -> soruce./<Name>/bin/activate
* Deactivate -> "deactivate"
* Delete venv by deleting the directory.

or venv in python3 (comes by default in python>3) except for creating venv -> * python3 -m venv <Name> *




