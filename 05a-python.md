# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> 1) List and tuples are collections of items or elements (other lists or tuples, strings, ints, floats, dictionaries, objects). 
>> Lists and tuples are indexed or keyed by integers starting at 0, thus giving them an inherent order. They also have associated methods that can be performed on them.
>> Both may be empty.
>> Lists and tuples differ in that lists are mutable - you may append, replace or remove items in a list. 
>> Tuples on the other hand are immutable, once they are created, they stay the way they are.
>> Tuples are handy if you know for sure that you don't want the data within to be erased, mutated, or added to.
   
>> 2) Tuples should work as keys in a dictionary, because they are immutable and they are hashable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> 1) Lists and sets are similar in that they are again collections of items or elements, which includes empty lists and sets. 
>> However, sets are unordered, and each element will be unique within the set.
>> Example: Starting with the list [1, 2, 2, 3] if it is converted to a set, the resulting elements will be 1, 2, 3

`In [7]: mylist = [1, 2, 2, 3]`

`In [8]: myset = set(mylist)`

`In [9]: mylist`
`Out[9]: [1, 2, 2, 3]`

`In [10]: myset`
`Out[10]: {1, 2, 3}` 

>> Both are iterable:

`In [6]: print [x ** 2 for x in mylist]`
`[1, 4, 4, 9]`

`In [7]: print [x ** 2 for x in myset]`
`[1, 4, 9]`

>> Finding whether an item is in a set is supposedly quicker than a list.
>> This is because for a set, apparently a hash table is searched, 
>> whereas for a list, you iterate over every item. 
>> Performance varies depending on the task though.
>> Found this interesting for this comparison:


`In [45]: In [42]: timeit.timeit('myset = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  ; 2 in myset', number = 100000)`
`Out[45]: 0.04457902908325195`

`In [46]: In [41]: timeit.timeit('mylst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  ; 2 in mylst', number = 100000)`
`Out[46]: 0.024330854415893555`

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are basically un-named or anonymous functions that have their own brief syntax.
>> For example, if we wanted to square a number, we might write a function such as that shown below.
>> Then we would call it with some argument, such as '7':

`In [27]: def square(number):`

  `....:     return number ** 2`

  `....: `

`In [28]: print square(7)`

`49`

>> Using a lambda function the whole process would be:

`In [30]: print (lambda x: x**2)(7)`

`49`

>> Lambda functions are usually used in a few situations:
>> 1) If the function is just a small function that will be used once,
>> it may be more convenient to just write it on one line. 
>> This allows code readability / simplicity.
>> Also, since the function is to be used only once,
>> it makes no sense for it to be named.

>> 2) Since a lambda function generates a function object, 
>> you may find instances where a function is a required argument,
>> and for simplicity and readability,
>> this could be accomplished on one line.

>> 3) Lambda functions are used for higher order functions:

>> Example: 

```
In [21]: def double_function(f, g):
   ....:     return lambda x: f(g(x))
   ....: 

In [22]: def add1(x):
   ....:     return x + 1
   ....: 

In [23]: def times2(x):
   ....:     return x * 2
   ....: 

In [24]: def square(x):
   ....:     return x * x
   ....: 

In [25]: def minus1(x):
   ....:     return x - 1
   ....: 

In [26]: calc1 = double_function(add1, square)

In [27]: calc2 = double_function(times2, minus1)

In [28]: calc3 = double_function(add1, minus1)

In [29]: calc1(5)
Out[29]: 26

In [30]: calc2(5)
Out[30]: 8

In [31]: calc3(5)
Out[31]: 5

In [32]: calc1(2)
Out[32]: 5

In [33]: calc2(2)
Out[33]: 2

In [34]: calc3(2)
Out[34]: 2

In [35]: calc1(square(3))
Out[35]: 82

In [36]: calc1(calc2(2))
Out[36]: 5
```

>> Lambda function using sorted:
>> Here, `sorted` will sort the animal list alphabetically,
>> but with a lambda function, 
>> we can sort by length of the name of each animal.
```
In [49]: animals = ['aardvark', 'pig', 'chicken', 'snuffleupagus', 'wombat', 'triceratops', 'ox', 'hippopotamus', 'duck', 'zebra', 'groundhog', 'rhinoceros']
```
```
In [50]: sorted(animals) # Sorts by alphabetical order - default
Out[50]: 
['aardvark',
 'chicken',
 'duck',
 'groundhog',
 'hippopotamus',
 'ox',
 'pig',
 'rhinoceros',
 'snuffleupagus',
 'triceratops',
 'wombat',
 'zebra']
```
```
In [51]: sorted(animals, key=lambda x: len(x)) # Sorts by length
Out[51]: 
['ox',
 'pig',
 'duck',
 'zebra',
 'wombat',
 'chicken',
 'aardvark',
 'groundhog',
 'rhinoceros',
 'triceratops',
 'hippopotamus',
 'snuffleupagus']
```


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way of generating a list from an iterable 
>> (a collection of items - such as a list, set, string, dictionary).
>> While generating the new list, 
>> you can manipulate each element that is placed in the new list,
>> or you can conditionally include or exclude items.
>> List comprehension basically replaces making a function or a method,
>> that includes a for loop. Once you are used to list comprehensions,
>> you can often save space. 


>> So, rather than:

```
list1 = [1, 3, 5, 7, 9]
def square(collection):
    squared_list = []
    for item in collection:
        squared_list.append(item ** 2)
    return squared_list

print square(list1)  

[1, 9, 25, 49, 81]
```

>> You can accomplish the same with:
```
print [item ** 2 for item in list1]

[1, 9, 25, 49, 81]
```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





