#### Exceptions/ Errors

Exceptions are python objects that represent errors. Different exceptions are raised for different reasons. 
Common exceptions:

- ImportError: an import fails.
- IndexError: a list is indexed with an out-of-range number.
- NameError: an unknown variable is used.
- SyntaxError: the code can't be parsed properly. 
- TypeError: a function is called on a value of an inappropriate type.
- ValueError: a function is called on a value of the correct type, but with an 
- inappropriate value.
- Unexpexted EOF: you forgot a colon or parenthesis or similar.

Exceptions occur when something goes wrong, due to incorrect code or input. When an exception occurs, the program immediately stops.
The following code produces the ZeroDivisionError exception by trying to divide 7 by 0:  
- `num1 = 7`
- `num2 = 0`
- `print(num1/num2)`

ZeroDivisionError: division by zero

#### Exception Handling

To handle exceptions, and to call code when an exception occurs, you can use a try/except statement. The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. If no error occurs, the code in the except block doesn't run.For example: 

- `try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")`

Result: 
An error occurred
due to zero division

What is the output of this code?
`try: 
variable=10
print(10/2)
except:
ZeroDivisionError:
print('Error')
print('Finished')`

answer: `5.0` `Finished`

A try statement can have multiple different except blocks to handle different exceptions. Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.

`try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")`

Result:
error occurred

An except statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes. For example:

`try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")`

Result: 
An error occurred

An except statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes. For example:

`try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")`

Result: 
An error occurred

#### Finally statement

To ensure some code runs no matter what errors occur, you can use a finally statement. The finally statement is placed at the bottom of a try/except statement. Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.

`try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")`

Result:
Hello
Divided by zero
This code will run no matter what

Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks. 

`try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   print(unknown_var)
finally:
   print("This is executed last")`

Result:
1
This is executed last

ZeroDivisionError: division by zero
During handling of the above exception, another exception occurred:
NameError: name 'unknown_var' is not defined

You can raise (intentionally create) exceptions by using the raise statement.

`print(1)
raise ValueError
print(2)

Result:
1
ValueError`

Which errors occur during evaluation of this code?

`try:
print(1/0)
except ZeroDivisionError:
raise ValueError`

Result:
ZeroDivisionError and ValueError

Exceptions can be raised with arguments that give detail about them. For example: 

`name = "123"
raise NameError("Invalid name!")`

Result: 
NameError: Invalid name!


In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
For example: 

`try:
   num = 5 / 0
except:
   print("An error occurred")
   raise`

An error occurred

ZeroDivisionError: division by zero



