# Loops, Conditions, and Parsing

In Bash scripting, loops and conditions are essential for controlling the flow of execution, while parsing allows manipulation of input data.

## Loops

### for loop
The `for` loop iterates over a list of items and executes a block of code for each item.

```bash
for item in list; do
    # commands
done
while loop
The while loop executes a block of code as long as a specified condition is true.

bash
Copy code
while condition; do
    # commands
done
until loop
The until loop executes a block of code until a specified condition becomes true.

bash
Copy code
until condition; do
    # commands
done
Conditions
if statement
The if statement executes a block of code based on the evaluation of a condition.

bash
Copy code
if condition; then
    # commands
fi
elif statement
The elif statement is used for additional condition checks in conjunction with if.

bash
Copy code
if condition1; then
    # commands
elif condition2; then
    # commands
fi
else statement
The else statement is used to execute a block of code if none of the previous conditions are true.

bash
Copy code
if condition; then
    # commands
else
    # commands
fi
Parsing
Internal Field Separator (IFS)
The IFS variable determines the delimiter used for word splitting during parsing.

bash
Copy code
IFS=delimiter
read command
The read command reads a line of input and assigns values to variables based on the delimiter specified by IFS.

bash
Copy code
read -r var1 var2 ...
Parsing Text
Parsing text involves breaking down a string or file into smaller parts for processing.

bash
Copy code
while IFS=delimiter read -r var1 var2 ...; do
    # commands
done < file.txt