text="Hello world"
result=text.lower()
result
'hello world'
greeting="good morning"
greeting.upper()
'GOOD MORNING'
data=" hello python "
data.strip()
'hello python'
line="Python is tough"
line.replace("tough","easy")
'Python is easy'
word="banana"
word.count("a")
3
>>> info="pyhon is fun"
>>> list(info).split(" ")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(info).split(" ")
AttributeError: 'list' object has no attribute 'split'
>>> info.split(" ")
['pyhon', 'is', 'fun']
>>> sentence="learn python"
>>> len(sentence)
12
>>> value="test123"
>>> value.isalnum()
True
>>> text="HELLO"
>>> text.lower()
'hello'
>>> text.capitalize()
'Hello'
>>> email='student@domain.com'
>>> email.endswith(".com")
True
>>> marks=[45,67,89,32]
>>> marks.sort()
>>> marks
[32, 45, 67, 89]
>>> numbers=[10,20,30]
>>> numbers.append(40)
>>> numbers
[10, 20, 30, 40]
>>> colors=['red','blue','green']
>>> colors.remove('blue')
>>> colors
['red', 'green']
>>> values=[1,2,3,2,1]
>>> values.count(2)
2
>>> items=['pen','book','pencil']
>>> items.join(",")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    items.join(",")
AttributeError: 'list' object has no attribute 'join'
>>> items.join(,)
SyntaxError: invalid syntax
>>> scores=[100,90,80]
>>> scores.reverse()
>>> scores
[80, 90, 100]
>>> a={1,2,3}
>>> b={2,3,4}
>>> a.union(b)
{1, 2, 3, 4}
>>> x={1,2,3}
>>> y={2,4}
>>> x.intersection(b)
{2, 3}
>>> numbers={5,10,15}
>>> numbers.add(20)
>>> numbers
{10, 20, 5, 15}
>>> marks={'ravi':90,'anu':85}
>>> marks=['sita':80]
SyntaxError: invalid syntax
>>> marks={'sita':80}
>>> marks
{'sita': 80}
>>> 