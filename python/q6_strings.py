# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    count = int(count)
    if count < 10:
        value = str(count)
    else:
        value = 'many'
    return 'Number of donuts: ' + value
    # raise NotImplementedError

# Tests:
# print donuts(4)
# print donuts(9)
# print donuts(10)
# print donuts(99)

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        value = ''
    else:
        value = s[:2] + s[-2:]
    return value 
    # raise NotImplementedError

# Tests:
# print both_ends('spring')
# print both_ends('Hello')
# print both_ends('a')
# print both_ends('xyz')

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    # Note: list(s[1:]) splits original word into a list starting at the first char
    return s[0] + ''.join(['*' if letter == s[0] else letter for letter in list(s[1:])])
    # raise NotImplementedError

# Tests:
# print fix_start('babble')
# print fix_start('aardvark')
# print fix_start('google')
# print fix_start('donut')

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    return b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]
    # raise NotImplementedError

# Tests:
# print mix_up('mix', 'pod')
# print mix_up('dog', 'dinner')
# print mix_up('gnash', 'sport')
# print mix_up('pezzy', 'firm')

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) < 3:
        return s
    else: 
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'
    # raise NotImplementedError

# Tests:
# print verbing('hail')
# print verbing('swiming')
# print verbing('do')


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    val_not = s.find("not")
    val_bad = s.find("bad")
    if val_not is not -1 and val_bad is not -1 and val_not < val_bad:
        # s_list = s.split()
        front = s[:val_not]
        back = s[val_bad + 3:]
        s = front + "good" + back
    return s

    #raise NotImplementedError
# Tests
# print not_bad('This movie is not so bad')
# print not_bad('This dinner is not that bad!')
# print not_bad('This tea is not hot')
# print not_bad("It's bad yet not")

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    pieces = []
    for string in [a, b]:
        if len(string) % 2 == 0:
            front = string[:len(string)/2]
            back = string[len(string)/2:]
        else:
            front = string[:len(string)/2 + 1]
            back = string[len(string)/2 + 1:]
        pieces.append(front)
        pieces.append(back)
    return pieces[0] + pieces[2] + pieces[1] + pieces[3]
    # raise NotImplementedError

# Tests:
# print front_back('123', '456')
# print front_back('1234', '4567')
# print front_back('abcd', 'xy')
# print front_back('abcde', 'xyz')
# print front_back('Kitten', 'Donut')


