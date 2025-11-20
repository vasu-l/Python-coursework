Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=list(map(int,input().split(",")))
print(l[:2])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    l=list(map(int,input().split(",")))
ValueError: invalid literal for int() with base 10: 'print(l[:2])'
>>> l=[1,1,2,40.40,69]
>>> l
[1, 1, 2, 40.4, 69]
>>> print(l[2])
2
>>> print(l[::2])
[1, 2, 69]
>>> print(keyword.kwlist)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(keyword.kwlist)
NameError: name 'keyword' is not defined
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
>>> print(matrix[1][2])
6
>>> print(matrix[2][0])
7
>>> list=[['srh','mi','rcb',][2,6,1]]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list=[['srh','mi','rcb',][2,6,1]]
TypeError: list indices must be integers or slices, not tuple
>>> list=[['srh','mi','rcb'][2,6,1]]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list=[['srh','mi','rcb'][2,6,1]]
TypeError: list indices must be integers or slices, not tuple
>>> list=[['srh','mi','rcb'],[2,6,1]]
>>> print(list)
[['srh', 'mi', 'rcb'], [2, 6, 1]]
>>> print(list[0][1])
mi
>>> print(list[0][0],[1][0])
srh 1
>>> teams=["srh","rcb",'mi','dc']
>>> print(teams)
['srh', 'rcb', 'mi', 'dc']
>>> print(teams.title())
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(teams.title())
AttributeError: 'list' object has no attribute 'title'
>>> teams=teams.split(" ")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    teams=teams.split(" ")
AttributeError: 'list' object has no attribute 'split'
>>> 