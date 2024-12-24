#Python Operators
'''Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:'''

#Example
print(10 + 5) #output 15

#Python divides the operators in the following groups:

'''Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
Python Arithmetic Operators'''

#Arithmetic operators are used with numeric values to perform common mathematical operations:

#'Operator, name and example;'
'+	Addition	    x + y'	
x = 5
y = 3
print(x + y) #output 8

'-	Subtraction	x - y'
x = 5
y = 3
print(x - y) #output 2

'*	Multiplication	x * y'
x = 5
y = 3
print(x * y) #output 15

'/	Division	x / y'
x = 12
y = 3
print(x / y) #output 4

'%	Modulus	x % y'	
x = 5
y = 2
print(x % y) #output 1

'**	Exponentiation	x ** y'
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2 # output 32

'//	Floor division	x // y'
x = 15
y = 2
print(x // y) #output 7
#the floor division // rounds the result down to the nearest whole number


#Python Assignment Operators
'Assignment operators are used to assign values to variables:'

#Operator	
'='	
x = 5 #same as	x = 5	
'+='	
x += 3	#same as x = x + 3	
'-='	
x -= 3 #same as	x = x - 3	
'*='
x *= 3 #same as	x = x * 3	
'/='
x /= 3 #same as	x = x / 3	
'%='
x %= 3 #same as x = x % 3	
'//='
x //= 3 #same as x = x // 3	
'**='
x **= 3 #same as x = x ** 3	
'&='
x &= 3 #same as	x = x & 3	
'|='
x |= 3 #same as	x = x | 3	
'^='
x ^= 3 #same as	x = x ^ 3	
'>>='	
x >>= 3 #same as x = x >> 3	
'<<='
x <<= 3 #same as x = x << 3	
':='	
print(x := 3) #same as x = 3 print(x)

#Python Comparison Operators

'Comparison operators are used to compare values and return boolean results:'

#'Operator, name and example;'
'>', 'Greater than', 5 > 3
'<', 'Less than', 5 < 3
'>=', 'Greater than or equal to', 5 >= 3
'<=','Less than or equal to', 5 <= 3
'==', 'Equal to', 5 == 3
'!=', 'Not equal to', 5 != 3
'is', 'Object identity', x is y


#Python Logical Operators
'Logical operators are used to combine conditional statements:'
#Operator, name and example
'and', 'Logical and', True and False
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

'or', 'Logical or', True or False
X = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

'not', 'Logical not', not True
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


#Python Identity Operators
'Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:'

#'Operator, name and example;'

'is', 'Object identity', x is y
x = 5
y = 5
print(x is y)
# returns True because x and y are actually the same object

'is not', 'Not object identity', x is not y
x = 5
y = 6
print(x is not y)
# returns True because x and y are not the same object

#Python Membership Operators
'Membership operators are used to test if a sequence is presented in an object:'

#Operator	Description	Example
'in',	'Returns True if a sequence with the specified value is present in the object',	x in y
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list


'not in',	'Returns True if a sequence with the specified value is not present in the object',	x not in y
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list


#Python Bitwise Operators
'Bitwise operators are used to compare (binary) numbers:'

'Operator', 'Name', 'Description',	'Example'
'&', 'AND',	'Sets each bit to 1 if both bits are 1',	x & y
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#'|', 'OR', 'Sets each bit to 1 if one of two bits is 1', x | y
print(6 | 3)

"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#'^',	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
print(6 ^ 3)

"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#~	NOT	Inverts all the bits	~x	
print(~3)

"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
4 = 0000000000000100
3 = 0000000000000011
2 = 0000000000000010
1 = 0000000000000001
0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""


#<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
print(3 << 2)

"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4= 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
8 = 0000000000001000
9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""	
#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
print(8 >> 2)

"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
8 = 0000000000001000
becomes
2 = 0000000000000010

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
8 = 0000000000001000
9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


#Operator Precedence
'Operator precedence describes the order in which operations are performed.'

#Example
'Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:'
print((6 + 3) - (6 + 3)) # (9)-(9) = 0


#Example
'Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:'

print(100 + 5 * 3)# 100 + 15 = 115

'The precedence order is described in the table below, starting with the highest precedence at the top:'

#Operator	Description	Try it
'''()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR	'''
note = 'If two operators have the same precedence, the expression is evaluated from left to right.'

#Example
'Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:'

print(5 + 4 - 7 + 3) #output is 5
'''The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5'''
