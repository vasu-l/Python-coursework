Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> teams=['srh','rcb','mi','dc']
>>> print(teams)
['srh', 'rcb', 'mi', 'dc']
>>> print(teams[::-1])
['dc', 'mi', 'rcb', 'srh']
>>> list=[1,2,4744,93939393]
>>> print(max(list))
93939393
>>> print(teams)
['srh', 'rcb', 'mi', 'dc']
>>> i=teams.sort()
>>> print(i)
None
>>> print(teams)
['dc', 'mi', 'rcb', 'srh']
>>> print(teams.sort)
<built-in method sort of list object at 0x0000023EF25F4DC0>
>>> print(teams.sort())
None
>>> teams.append("rr','rcb')
	     
SyntaxError: EOL while scanning string literal
>>> print(teams)
['dc', 'mi', 'rcb', 'srh']
>>> teams.append("rr",'rcb')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    teams.append("rr",'rcb')
TypeError: list.append() takes exactly one argument (2 given)
>>> teams.extend("rr",'rcb')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    teams.extend("rr",'rcb')
TypeError: list.extend() takes exactly one argument (2 given)
>>> teams.extends("rr")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    teams.extends("rr")
AttributeError: 'list' object has no attribute 'extends'
>>> teams.append("rr")
>>> teams.extend("rcb")
>>> print(teams)
['dc', 'mi', 'rcb', 'srh', 'rr', 'r', 'c', 'b']
>>> teams
['dc', 'mi', 'rcb', 'srh', 'rr', 'r', 'c', 'b']
>>> print(teams.startswith("r"))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(teams.startswith("r"))
AttributeError: 'list' object has no attribute 'startswith'
>>> i=teams.startswith("r")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    i=teams.startswith("r")
AttributeError: 'list' object has no attribute 'startswith'
>>> for i in teams:
	if i.startswith("r"):
		print(i)

		
rcb
rr
r
>>> for i in teams:
	if i.endswith('i')
	
SyntaxError: invalid syntax
>>> for u in teams:
	if u.endswith('i'):
		print(u)

		
mi
>>> n=[1,2,3,4,5]
>>> for i in n:
	if i%2==0:
		print(i)

		
2
4
>>> print(i/n)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(i/n)
TypeError: unsupported operand type(s) for /: 'int' and 'list'
>>> for i in n:
	if i&2==0:
		print(i, "is a even number")
	else:
		print(i, "is a odd number")

		
1 is a even number
2 is a odd number
3 is a odd number
4 is a even number
5 is a even number
>>> for i in n:
	if i%2==0:
		print(i, "is a even number")
	else:
		print(i, "is a odd number")

		
1 is a odd number
2 is a even number
3 is a odd number
4 is a even number
5 is a odd number
>>> numbers=[10,25,3,45,25,60]
>>> print(numbers.index[25])
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(numbers.index[25])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> numbers.index[25]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    numbers.index[25]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> numbers.index(25)
1
>>> numbers.insert(2,35)
>>> numbers
[10, 25, 35, 3, 45, 25, 60]
>>> numbers.pop()
60
>>> i=numbers.copy()
>>> i
[10, 25, 35, 3, 45, 25]
>>> numbers.clear()
>>> numbers
[]
>>> for i in numbers:
	if i%2==0:
		print(i*2)

		
>>> numbers
[]
>>> numbers=[10, 25, 35, 3, 45, 25, 60]
>>> 
KeyboardInterrupt
>>> for i in numbers:
	if i%2==0:
		print(i*2)

20
120
>>> numbers.sort()
>>> print(numbers[-2])
45
>>> numbers
[3, 10, 25, 25, 35, 45, 60]
>>> words=['apple','banana','cherry','date']
>>> for i in words:
	if i.startswith("a,e,i,o,u"):
		print(i)

		
>>> vowels="a",'e','i''o','u'
>>> 
KeyboardInterrupt
>>> for i in words:
	if i.startswith(vowels):
		print(i)

		
apple
>>> words.append('orange')
>>> for i in words:
	if i.startswith(vowels):
		print(i)

		
apple
>>> words
['apple', 'banana', 'cherry', 'date', 'orange']
>>> for i in words:
	if i.startswith(vowels):
		print(i)

apple
>>> 