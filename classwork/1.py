Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> teams=['srh','mi','csk','bsdk','mi']
>>> set(teams)
{'mi', 'srh', 'csk', 'bsdk'}
>>> list(teams)
['srh', 'mi', 'csk', 'bsdk', 'mi']
>>> list(set(teams))
['mi', 'srh', 'csk', 'bsdk']
>>> ipl=['mi','csk','dc','rr','srh','rcb']
>>> list(set(teams)+set(ipl))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(set(teams)+set(ipl))
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> list(set(teams+ipl))
['rcb', 'dc', 'mi', 'csk', 'srh', 'bsdk', 'rr']
>>> tuple(list)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(list)
TypeError: 'type' object is not iterable
>>> tuple(teams)
('srh', 'mi', 'csk', 'bsdk', 'mi')
>>> n=int(input())
for i in n:
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    n=int(input())
ValueError: invalid literal for int() with base 10: 'for i in n:'
>>> 