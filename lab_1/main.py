#1. WAP to demonstrate diffenet data types and arithematic operations ...
# __main__ segment
''' All numeric types '''
int_val = 10
float_val = 50.03
complex_val = 2 + 3.4j
bool_val = 1 # subtype of plain int
''' characters and strings '''
str_val = 'hello'
''' Ordered collection types '''
list_val = [int_val,float_val,bool_val,complex_val,str_val]
tuple_val = (int_val,float_val,bool_val,complex_val,str_val)
''' Unordered unique collection types '''
set_val = {1,2.345,'hello'}
''' Unordered mapping types '''
dict_val = {'emp_id':110011,'emp_name':'Ram Prasad'}
# Printing the data types
print("Data Types:")
print(f'int_val is of type {type(int_val)} and value: {int_val}')
print(f'float_val is of type {type(float_val)} and value: {float_val}')
print(f'complex_val is of type {type(complex_val)} and value: {complex_val}')
print(f'str_val is of type {type(str_val)} and value: "{str_val}"')
print(f'list_val is of type {type(list_val)} and value: {list_val}')
print(f'tuple_val is of type {type(tuple_val)} and value: {tuple_val}')
print(f'set_val is of type {type(set_val)} and value: {set_val}')
print(f'dict_val is of type {type(dict_val)} and value: {dict_val}')
print(f'bool_val is of type {type(bool_val)} and value: {bool_val}')

# __________________ Arithematic operations __________________
num1 = 10
num2 = 35
print("\nArithmetic Operations:")
# Addition
print(f'Addition: {num1} + {num2} = {num1 + num2}')
# Subtraction
print(f'Subtraction: {num1} - {num2} = {num1 - num2}')
# Multiplication
print(f'Multiplication: {num1} * {num2} = {num1 * num2}')
# Division
print(f'Division: {num1} / {num2} = {num1 / num2}')
# Floor Division
print(f'Floor Division: {num1} // {num2} = {num1 // num2}')
# Modulus
print(f'Modulus: {num1} % {num2} = {num1 % num2}')
# Exponentiation
print(f'Exponentiation: {num1} ** {num2} = {num1 ** num2}')

