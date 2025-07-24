# BaseScript
**A basic programming language. Interpreted to Python 3.13.2.**

> ### ⚠️ Windows versions below Windows 10 are not supported
## Usage
### Installation
1. Download the newest release on the GitHub page
2. Place the file in a directory, that has been added to PATH (e.g. C:\)
### Shell
In order to use BaseScript shell, run the command ``basescript`` in the command line
### File
In order to use BaseScript to run a BS file, run the command ``basescript filename.bs`` in the command line
### Build
In order to build a BS file to a Python 3.13.2 file, run the command ``basescript filename.bs build=filename.py``. This will generate a working Python file , that can be run with Python 3.13.2.

## Statements
### Control statements
 - **if**  
 **Description**: Conditional statement. If the boolean expression is True, the code within the block is executed.  
 **Syntax**: `if <boolean-expression>: {...};`  

 - **return**  
 **Description**: Returns the value of the expression, and stops the execution of the function.  
 **Syntax**: `return <expression>;`  

### Loop statements
 - **repeat**  
 **Description**: Repeat a block of code a specified number of times.  
 **Syntax**: `repeat <binary-expression, boolean-expression or numeric-expression>: {...};`  

### Declaration statements
 - **var**  
 **Description**: Declare a variable. The type of the variable is determined by the assigned value.  
 **Syntax**: `var <identifier> = <expression>;`  

 - **func**  
 **Description**: Declare a function. This function can later be called with the `call` statement or expression.  
 **Syntax**: `func <identifier>([parameters]): {...};`  

### Extra statements
 - **log**  
 **Description**: Log a message to the console.  
 **Syntax**: `log <expression>;`  

## Expressions
### Literal expressions
 - **True** and **False**: `True` `False`
 - **Strings**: `"string"`
 - **Numbers**: `0-9`
 - **Binary**: `<numeric-expression relational-operator numeric-expression>`
### Variable expressions
 - **Variable**: `<identifier>`
 - **Boolean**: `<<expression> <operator> <expression>>` (the expressions and operator are literally between angle brackets)
 - **Input**: `input <expression>`
 - **Call**: `call <function-identifier>([parameters])`
 - **Pycall**: `pycall <python-function-identifier>([parameters])`

## Operators
### Arithmetic operators
 - **+** : Addition
 - **-** : Subtraction
 - **\*** : Multiplication
 - **/** : Division
### Relational operators
 - **is**: Compares two expressions, returns `True` when equal, and `False` when not equal.
 - **isnt**: Compares two expressions, returns `False` when equal, and `True` when not equal.
 - **gt**: Compares two expressions, returns `True` when the first is greater than the second, returns `False` when the first is smaller than the second.
 - **lt**: Compares two expressions, returns `False` when the first is greater than the second, returns `True` when the first is smaller than the second.
