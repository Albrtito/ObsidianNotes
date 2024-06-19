---
aliases:
  - Static Method
tags:
  - python
  - SoftwareDev
"References:":
  - https://pythonbasics.org/static-method/
cssclasses:
---
Static methods in python are used in order to call a function inside of a class without the need of creating an object of said function. 

See the following example: The methods PrintHello will need for an object of MyClass to be created. While the method PrintAdios does not need that. It can be directly called by: `MyClass.PrintAdios()`

+ See that the **static method does not require the self parameter**
+ See that the static method is not called from an object but directly from a a class

```python
class MyClass(object): 

	def PrintHello(self):
		print("Hello")
	@staticmethod
	def PrintAdios():
		print("Adios")

```
