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
>> For example, if we wanted to square a number, we might write a function such as this:

`In [27]: def square_it(number):`
  `....:     return number ** 2`
  `....: `

`In [28]: print square_it(7)`
`49`

>> Using a lambda function the whole process would be:

`In [30]: print (lambda x: x**2)(7)
49`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

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





