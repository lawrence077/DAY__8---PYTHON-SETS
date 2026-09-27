Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
names= {"lawrence", "james", "cristiano"}
print(names)
{'james', 'lawrence', 'cristiano'}
names= {"lawrence", "james", "cristiano", "peter"}
print(names)
{'james', 'peter', 'lawrence', 'cristiano'}
names= {"lawrence", "james", "cristiano", "peter", "lawrence"}
print(names)
{'james', 'peter', 'lawrence', 'cristiano'}
{'james', 'peter', 'lawrence', 'cristiano'}
{'james', 'peter', 'lawrence', 'cristiano'}
names= set()
print(names)
set()
names= {"lawrence", "james", "cristiano"}
names.add("peter")
print(names)
{'james', 'peter', 'lawrence', 'cristiano'}
names= {"lawrence", "james", "cristiano"}
names.remove("james")
print(names)
{'lawrence', 'cristiano'}
names= {"lawrence", "james", "cristiano"}
names.update({"peter", "david", "sam"})
print(names)
{'david', 'peter', 'sam', 'cristiano', 'james', 'lawrence'}
names= {"lawrence", "james", "cristiano"}
names.discard("peter")
print(names)
{'james', 'lawrence', 'cristiano'}
names= {"lawrence", "james", "cristiano"}
names.pop()
'james'
print(names)
{'lawrence', 'cristiano'}
names= {"lawrence", "james", "cristiano"}
names.clear()
print(names)
set()
names= {"lawrence", "james", "cristiano"}
a= {"lawrence", "john"}
b= {"peter", "david"}
c= a.union(b)
print(c)
{'david', 'peter', 'lawrence', 'john'}
names= {"lawrence", "james", "cristiano"}
KeyboardInterrupt
KeyboardInterrupt
a= {"lawrence", "james", "cristiano"}
b= {"peter", "david", "john"}
c= a.intersection(b)
print(c)
set()
a= {"lawrence", "james", "cristiano"}
b= {"peter", "james", "cristiano"}
c= a.intersection(b)
print(c)
{'james', 'cristiano'}
a= {"lawrence", "james", "cristiano"}
b= {"james", "david"}
c= a.difference(b)
>>> print(c)
{'lawrence', 'cristiano'}
>>> a= {"lawrence", "james", "cristiano"}
>>> b= {"james", "david"}
>>> c =a.symmetric_difference(b)
>>> print(c)
{'david', 'lawrence', 'cristiano'}
>>> a= {"lawrence", "james", "cristiano"}
>>> b= {"lawrence", "james", "cristiano"}
>>> print(a.issubset(b))
True
>>> a= {"lawrence", "james", "cristiano"}
>>> b= {"james","cristiano"}
>>> print(a.issuperset(b))
True
>>> a= {"lawrence", "james", "cristiano"}

>>> b= {"james", "david"}
>>> print(a.isdisjoint(b))
False
>>> KeyboardInterrupt
>>> KeyboardInterrupt
>>> names= {"lawrence", "james", "cristiano"}
>>> new name= names.copy()
SyntaxError: invalid syntax
>>> new_name= names.copy()
>>> print(new_name)
{'james', 'lawrence', 'cristiano'}
