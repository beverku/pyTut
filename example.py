#!/usr/bin/env python3.5 -tt

# -*- coding: ascii -*-
"""-tt tells python to stop if there is mixed tabs and spaces in the file"""

import unittest
import re
import math
import json
import random


globalVar1 = 1


class TestExample(unittest.TestCase):
    """Example of python language basics as a unit test.
    """

    ##################################
    # Falsey
    ##################################
    def test_Falsey(self):
	# tab
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse('')

        self.assertTrue('0')

        # empty Sequences i.e. list, set, dict, tuple are false
        self.assertFalse([])
        self.assertFalse(set())
        self.assertFalse({})
        self.assertFalse(())



    ##################################
    # Arithmetic
    ##################################
    def test_arithmetic(self):
        # Python only stores about 15 digits of a float
        f = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899
        self.assertEqual(3.141592653589793, f)

        # Notice it rounds - not truncate
        f = 0.123456789012345678
        self.assertEqual(0.12345678901234568, f)




    ##################################
    # Strings
    ##################################
    def test_strings(self):

        # Can use '' or ""
        s = "can't"
        self.assertEqual('can\'t', s)

        s = 'She said: "I love python"'
        self.assertEqual("She said: \"I love python\"", s)

        # len
        self.assertEqual(5, len('Hello'))

        # index
        s = 'Hello'
        self.assertEqual('e', s[1])

        # But they are immutable
        with self.assertRaises(TypeError):
            s[0] = 'c'

        # String cat with + operator
        s = 'word1' + ' ' + 'word2'
        self.assertEqual('word1 word2', s)

        # Unlike Java you can't cat a string an int
        with self.assertRaises(TypeError):
            x = 'word1' + 3
            print(x)
        self.assertEqual('word13', 'word1' + str(3))

        # Two or more string LITERALS are automatically concatenated
        s = 'I am ' 'a string'
        self.assertEqual('I am a string', s)

        s = (
            'Which is probably more useful '
            'when used like this.  '
            'To create more readable code.'
        )
        self.assertEqual('Which is probably more useful when used like this.  To create more readable code.', s)

    def test_strings_split(self):

        # split() with no arg splits on white
        l = 'This is a string\twith\n\n\twhite'.split()
        self.assertEqual( ['This', 'is', 'a', 'string', 'with', 'white'], l)

    def test_strings_slice(self):

        # One way to remember how slices work is to think of the indices as pointing between characters,
        # with the left edge of the first character numbered 0.
        # Then the right edge of the last character of a string of n characters has index n, for example:
        # +---+---+---+---+---+---+
        # | P | y | t | h | o | n |
        # +---+---+---+---+---+---+
        # 0   1   2   3   4   5   6
        # -6 -5  -4  -3  -2  -1

        # s[start:end] # substring start through end-1
        # s[start:]    # substring start through the rest of the String
        # s[:end]      # substring from the beginning through end-1
        # s[:]         # a copy of the whole String
        # s[start:end:step] # start through not past end, by step
        # The key point to remember is that the :end value represents the first value that is NOT in the selected slice. 
        s = 'Hello'
        self.assertEqual('el', s[1:3])
        self.assertEqual('ello', s[1:])
        self.assertEqual('Hel', s[:3])
        self.assertEqual('Hello', s[:])
        self.assertEqual('Hlo', s[::2])

        # The other feature is that start or end may be a negative number, which means it counts
        # from the end of the String instead of the beginning. So:
        # s[-1]    # last character in the String
        # s[-2:]   # last two substring in the String
        # s[:-2]   # everything except the last two substring
        self.assertEqual('e', s[-4])
        self.assertEqual('lo', s[-2:])
        self.assertEqual('Hel', s[:-2])

        # Python is kind to the programmer if there are fewer characters than you ask for. 
        # For example, if you ask for a[:-2] and a only contains one character, you get an
        # empty String instead of an error.
        # Sometimes you would prefer the error, so you have to be aware that this may happen.
        self.assertEqual('ello', s[1:99])
        self.assertEqual('Hello', s[-99:])
        self.assertEqual('', s[:-99])

        # Also can be important that [:] returns a shallow copy of a list. it means that every
        # slice notation returns a list which have new address in memory,
        # but its elements would have same addresses that elements of source list have.

    def test_strings_methods(self):
        # Use string methods instead of the string module.
        # String methods are always much faster and share the same API
        # with unicode strings.

        # Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.
        # startswith() and endswith() are cleaner and less error prone.
        # For example:

        # Yes:
        foo = 'bar'
        self.assertTrue(foo.startswith('bar'))

        # No:
        self.assertTrue(foo[:3] == 'bar')

    def test_strings_format(self):
        # Basic usage of the str.format() method looks like this:
        formatted = 'We are the {} who say "{}!"'.format('knights', 'Ni')
        self.assertEqual('We are the knights who say "Ni!"', formatted)

        # positional
        formatted = '{0} and {1}'.format('spam', 'eggs')
        self.assertEqual('spam and eggs', formatted)

        formatted = '{1} and {0}'.format('spam', 'eggs')
        self.assertEqual('eggs and spam', formatted)

        # keyword
        formatted = 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
        self.assertEqual('This spam is absolutely horrible.', formatted)

        # An optional ':' and format specifier can follow the field name.
        # This allows greater control over how the value is formatted.

        # float
        formatted = 'The value of PI is approximately {0:.3f}.'.format(math.pi)
        self.assertEqual('The value of PI is approximately 3.142.', formatted)

        # space separated
        formatted = '{0:10} ==> {1:10d}'.format('a name', 1234)
        #                 1234567890 ==> 1234567890
        self.assertEqual('a name     ==>       1234', formatted)

        # strings are r-padded and integers l-padded
        formatted = '{0:10} ==> {1:10}'.format('a name', 'b name')
        #                 1234567890 ==> 1234567890
        self.assertEqual('a name     ==> b name    ', formatted)

        # integers l-padded
        formatted = '{0:10d} ==> {1:10d}'.format(1234, 567)
        #                 1234567890 ==> 1234567890
        self.assertEqual('      1234 ==>        567', formatted)

    def test_strings_old_style_format(self):

        # The % operator can also be used for string formatting.
        # It interprets the left argument much like a sprintf()-style format string to be applied to the right argument,
        # and returns the string resulting from this formatting operation.For example:

        formatted = 'The value of PI is approximately %5.3f.' % math.pi
        self.assertEqual('The value of PI is approximately 3.142.', formatted)

        formatted = 'an int: %05d' % 123
        self.assertEqual('an int: 00123', formatted)




    ##################################
    # For Loops
    ##################################
    def test_for_loops(self):

        # If you need to modify the sequence you are iterating over while inside the loop,
        # it is recommended that you first make a copy.
        # Iterating over a sequence does not implicitly make a copy.
        # The slice notation makes this especially convenient:
        words = ['one', 'two', 'four']
        for w in words[:]:
            if w == 'two':
                words.insert(0, 'zero')

        self.assertEqual(['zero', 'one', 'two', 'four'], words)

        # When looping through a sequence, the position index and corresponding value
        # can be retrieved at the same time using the enumerate() function.
        # Paired with tuple unpacking makes it very nice
        d = {}
        for index, val in enumerate(['tic', 'tac', 'toe']):
            d[index] = val
        self.assertEqual({0: 'tic', 1: 'tac', 2: 'toe'}, d)

        # To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
        d = {}
        questions = ['name', 'quest', 'favorite color']
        answers = ['lancelot', 'the holy grail', 'blue']
        for q, a in zip(questions, answers):
            d[q] = a
        self.assertEqual({'name': 'lancelot', 'quest': 'the holy grail', 'favorite color': 'blue'}, d)

        # When looping through dictionaries, the key and corresponding value can
        # be retrieved at the same time using the items() method.
        # Paired with tuple unpacking makes it very nice
        d = {}
        knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        for key, val in knights.items():
            d[val] = key
        self.assertEqual({'the pure': 'gallahad', 'the brave': 'robin'}, d)


    ##################################
    # Lists
    ##################################
    def test_lists(self):
        # References to lists are pointers
        a = [1, 2, 3]
        b = a
        self.assertEqual([1, 2, 3], a)
        self.assertEqual([1, 2, 3], b)

        # Changes made to a are reflected in b
        a[0] = 0
        a.append(4)
        self.assertEqual([0, 2, 3, 4], a)
        self.assertEqual([0, 2, 3, 4], b)

        # Use "in" keyword to test
        a = [1, 2, 3]
        self.assertTrue(1 in a)
        self.assertFalse(4 in a)

    def test_lists_copy(self):
        # to (shallow) copy the array use slice
        a = [1, 2, 3]
        b = a[:]
        self.assertEqual([1, 2, 3], a)
        self.assertEqual([1, 2, 3], b)

        # Changes made to a are NOT reflected in b
        # Note if these were objects changes to the object would be reflected in b
        a[0] = 0
        a.append(4)
        self.assertEqual([0, 2, 3, 4], a)
        self.assertEqual([1, 2, 3], b)

    def test_lists_slice(self):
        # a[start:end] # items start through end-1
        # a[start:]    # items start through the rest of the array
        # a[:end]      # items from the beginning through end-1
        # a[:]         # a copy of the whole array
        # a[start:end:step] # start through not past end, by step
        # The key point to remember is that the :end value represents the first value that is NOT in the selected slice. 
        l = [0, 1, 2, 3, 4]
        self.assertEqual([1, 2], l[1:3])
        self.assertEqual([1, 2, 3, 4], l[1:])
        self.assertEqual([0, 1, 2], l[:3])
        self.assertEqual([0, 1, 2, 3, 4], l[:])
        self.assertEqual([0, 2, 4], l[::2])

        # The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:
        # a[-1]    # last item in the array
        # a[-2:]   # last two items in the array
        # a[:-2]   # everything except the last two items
        self.assertEqual(1, l[-4])
        self.assertEqual([3, 4], l[-2:])
        self.assertEqual([0, 1, 2], l[:-2])

        # Python is kind to the programmer if there are fewer items than you ask for. 
        # For example, if you ask for a[:-2] and a only contains one element, you get an empty list instead of an error. 
        # Sometimes you would prefer the error, so you have to be aware that this may happen.
        self.assertEqual([1, 2, 3, 4], l[1:99])
        self.assertEqual([0, 1, 2, 3, 4], l[-99:])


        # Also can be important that [:] returns a shallow copy of a list. it means that every slice notation returns a list which have new address in memory, 
        # but its elements would have same addresses that elements of source list have.

        # Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
        l = [0, 1, 2, 3, 4]
        l[1:3] = [-1, -2]
        self.assertEqual([0, -1, -2, 3, 4], l)

        l = [0, 1, 2, 3, 4]
        l[1:3] = []
        self.assertEqual([0, 3, 4], l)

    def test_lists_append_extend(self):
        # append returns None - So don't do l = l.append(x)
        l = [1, 2, 3]
        self.assertIsNone(l.append(4))
        self.assertEqual([1, 2, 3, 4], l)

        # append: Appends object at end.
        l = [1, 2, 3]
        l.append([4, 5])
        self.assertEqual([1, 2, 3, [4, 5]], l)  # Notice element 3 is a list

        # extend: Extends list by appending elements from the iterable.
        l = [1, 2, 3]
        l.extend([4, 5])
        self.assertEqual([1, 2, 3, 4, 5], l)  # Notice elements appended

        # You can also use concatenation to extend
        l = [1, 2, 3]
        l += [4, 5]
        self.assertEqual([1, 2, 3, 4, 5], l)  # Notice elements appended



    def test_lists_pop(self):
        l = [1, 2, 3]
        item = l.pop()
        self.assertEqual(3, item)
        self.assertEqual([1, 2], l)

        l = [1, 2, 3, 4]
        item = l.pop(1)
        self.assertEqual(2, item)
        self.assertEqual([1, 3, 4], l)

    def test_lists_sorted(self):
        # sorted returns a new list and l is unchanged
        l = [5, 2, 3, 1, 4]
        sl = sorted(l)
        self.assertEqual([1, 2, 3, 4, 5], sl)
        self.assertEqual([5, 2, 3, 1, 4], l)

        # Default sort is the natural sort
        # But you can use a custom key - Which is not a traditional comparator
        # but instead returns a shadow list that is then used to sort
        # so we can sort on the len() function which on takes a single parameter
        l = ['dd', 'z', 'aaa', 'bbb', 'cc']
        sl = sorted(l, key=len)
        self.assertEqual( [ 'z', 'dd', 'cc', 'aaa', 'bbb'] , sl)

        # Notice this also demonstrates that the sorted method is stable

    def test_lists_comprehension(self):

        # List comprehensions provide a concise way to create lists.
        l = [ 'aaaa', 'bb', 'ccc' ]
        l2 = [ len(s)   for s in l ]
        self.assertEqual( [4, 2, 3], l2 ) 

        # They can apply a filter
        l = range(10)
        evenSquares = [ x**2   for x in l   if x % 2 == 0 ]
        self.assertEqual( [0, 4, 16, 36, 64], evenSquares ) 

        l = range(10)
        squareTuples = [  (x, x**2)   for x in l   if x % 2 == 0 ]
        self.assertEqual( [ (0, 0), (2, 4), (4, 16), (6, 36), (8, 64) ], squareTuples )



    ##################################
    # Sets
    ##################################
    def test_sets(self):
        # A set is an unordered collection with no duplicate elements.
        # Basic uses include membership testing and eliminating duplicate entries.
        # Set objects also support mathematical operations like
        # union, intersection, difference, and symmetric difference.

        # Curly braces or the set() function can be used to create sets.
        a = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
        self.assertEqual({'orange', 'banana', 'pear', 'apple'}, a)

        # Note: to create an empty set you have to use set(), not {}
        # the latter creates an empty dictionary
        b = set()
        self.assertEqual(0, len(b))

        # fast membership testing
        self.assertTrue('orange' in a)

        # unordered and no duplicates
        self.assertTrue({1, 2} == {2, 1, 2, 1})

        # Demonstrate set operations on unique letters from two words
        a = set('abracadabra')
        b = set('alacazam')

        # letters in a but not in b
        c = a - b
        self.assertEqual({'r', 'd', 'b'}, c)

        # letters in either a or b
        c = a | b
        self.assertEqual({'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}, c)

        # letters in both a and b
        c = a & b
        self.assertEqual({'a', 'c'}, c)

        # letters in a or b but not both
        c = a ^ b
        self.assertEqual({'r', 'd', 'b', 'm', 'z', 'l'}, c)

        # Set comprehension
        c = {x for x in 'abracadabra' if x not in 'abc'}
        self.assertEqual({'r', 'd'}, c)



    ##################################
    # Tuples
    ##################################
    def test_tuples(self):
        # tuples are defined with ()

        # empty tuple
        t = ()
        self.assertEqual(0, len(t))

        # defining a tuple of one is quirky
        t = (1,)    # Notice trailing comma
        self.assertEqual(1, len(t))
        # Also
        t = 1,    # Notice trailing comma
        self.assertEqual(1, len(t))

        t = (1, 2, 3)
        self.assertEqual((1, 2, 3), t)
        # This is called tuple packing
        t = 1, 2, 3
        self.assertEqual((1, 2, 3), t)

        # Access with []
        self.assertEqual(1, t[0])

        # Tuples are immutable
        with self.assertRaises(TypeError):
            t[0] = 0
                
        # Tuple unpacking
        t = (1, 2)
        (x, y) = t
        self.assertEqual(1, x) 
        self.assertEqual(2, y)
        # Also
        x, y = t
        self.assertEqual(1, x)
        self.assertEqual(2, y)


    ##################################
    # Named Tuples
    ##################################
    def test_named_tuples(self):

        # This is a color tuple, but how do we know that
        p = (170, 0.1, 0.6)
        hue = p[0]
        saturation = p[1]
        luminosity = p[2]

        # Named Tuples make the code self documenting
        from collections import namedtuple
        Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])
        p = Color(170, 0.1, 0.6)
        hue = p.hue
        saturation = p.saturation
        luminosity = p.luminosity


    ##################################
    # Dictionaries
    ##################################
    def test_dictionaries(self):
        # dictionaries are indexed by keys, which can be any immutable type;
        # strings and numbers can always be keys.
        # Tuples can be used as keys if they contain only strings, numbers, or tuples;
        # if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.

        # dictionaries are defined with {}
        d = {}
        self.assertEqual(0, len(d))

        d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
        self.assertEqual('val1', d['key1'])
        self.assertEqual('val2', d['key2'])
        self.assertEqual('val3', d['key3'])

        # Also dict() constructor
        d = dict([('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3')])
        self.assertEqual('val1', d['key1'])
        self.assertEqual('val2', d['key2'])
        self.assertEqual('val3', d['key3'])

        # You can Access/Assign with []
        d['key1'] = 'val1'
        d['key2'] = 'val2'
        d['key3'] = 'val3'
        self.assertEqual('val1', d['key1'])
        self.assertEqual('val2', d['key2'])
        self.assertEqual('val3', d['key3'])

        # But Accessing a non-existent key is an error
        with self.assertRaises(KeyError):
            x = d['noSuchKey']

        # There is a .get method that will retrun the value or None
        self.assertEqual('val1', d.get('key1'))
        self.assertIsNone(d.get('noSuchKey'))

        # Use "in" keyword to test
        self.assertTrue('key1' in d )
        self.assertFalse('noSuchKey' in d )

        # keys / values
        self.assertEqual(['key1', 'key2', 'key3'], sorted(d.keys())) # sorted needed because order is not guaranteed
        self.assertEqual(['val1', 'val2', 'val3'], sorted(d.values())) # sorted needed because order is not guaranteed

        # items - returns key/value as a tuple
        # sorted needed because order is not guaranteed
        self.assertEqual([('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3')], sorted(d.items()))

        # Dictionary comprehension
        d = {x: x ** 2 for x in (2, 4, 6)}
        self.assertEqual({2: 4, 4: 16, 6: 36}, d)

        # Dictionary comprehension - 2
        chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
        # This will swap the keys and values
        # Dictionary comprehension  tuple unpacking
        rank_dict = {rank: name for name, rank in chile_ranks.items()}
        self.assertEqual({1: 'ghost', 2: 'habanero', 3: 'cayenne'}, rank_dict)


    ##################################
    # Read/Write files
    ##################################
    def test_read_files(self):

        # Open for reading U with universal line endings i.e. \n or \r or \r\n
        file1 = open('./file1.txt', 'rU')
        file1.close()

        # The with statement allows objects to be cleaned up properly
        with open('./file1.txt', 'rU') as file1:
            pass

        # This will read the file line by line
        s = ''
        with open('./file1.txt', 'rU') as file1:
            for line in file1:
                s += line
        # Notice newlines are still there
        self.assertEqual('line1\nline2\nline3 word2\n', s)

        # This will read all lines into a list
        with open('./file1.txt', 'rU') as file1:
            lines = file1.readlines()
        # Notice newlines are still there
        self.assertEqual(['line1\n', 'line2\n', 'line3 word2\n'], lines)

        # This will ALSO read all lines into a list
        with open('./file1.txt', 'rU') as file1:
            lines = list(file1)
        # Notice newlines are still there
        self.assertEqual(['line1\n', 'line2\n', 'line3 word2\n'], lines)

        # This will read the entire file into a String
        with open('./file1.txt', 'rU') as file1:
            s = file1.read()
        self.assertEqual('line1\nline2\nline3 word2\n', s)

    def test_write_files(self):
        # Write a String
        with open('./out.txt', 'w') as fout:
            fout.write('a String')
        with open('./out.txt', 'rU') as f:
            self.assertEqual('a String', f.read())

        # Write a List
        with open('./out.txt', 'w') as fout:
            fout.writelines(['line1', 'line2', 'line3'])
        with open('./out.txt', 'rU') as f:
            # Notice no newlines
            self.assertEqual('line1line2line3', f.read())

        # Write a List - With newlines
        with open('./out.txt', 'w') as fout:
            fout.writelines(map(lambda line: line + '\n', ['line1', 'line2', 'line3']))
        with open('./out.txt', 'rU') as f:
            # Notice newlines
            self.assertEqual('line1\nline2\nline3\n', f.read())


    ##################################
    # Read/Write JSON
    ##################################
    def test_read_json(self):

        # python object to json string
        json_string = json.dumps([1, 'simple', 'list'])
        self.assertEqual('[1, "simple", "list"]', json_string)

        # Notice this the dictionary looks a lot like json anyway
        json_string = json.dumps({'key1': 'val1', 'key2': 'val2', 'key3': 3})
        self.assertTrue('"key1": "val1"' in json_string)
        self.assertTrue('"key2": "val2"' in json_string)
        self.assertTrue('"key3": 3' in json_string)

        # Load from json
        l = json.loads('[1, "simple", "list"]')
        self.assertEqual([1, 'simple', 'list'], l)

        d = json.loads('{"key1": "val1", "key3": 3, "key2": "val2"}')
        self.assertEqual({'key1': 'val1', 'key2': 'val2', 'key3': 3}, d)

        # Note there are corresponding dump and load (without the trailing s) for file json





    ##################################
    # Regex
    ##################################
    def test_re(self):
        # re.search returns a match opbject
        # a leading r before a string - indicates it's a raw string - don't do any \ escaping etc.
        match = re.search(r'([\w.]+)@([\w.]+)', 'blah blah ryan.bever@netapp.com blah blah')
        if match:
            self.assertEqual('ryan.bever@netapp.com', match.group() )  # group() is the entire match
            self.assertEqual('ryan.bever', match.group(1) ) # group(i) is the individual group
            self.assertEqual('netapp.com', match.group(2) )

        # a non-match returns None
        self.assertIsNone( re.search(r'dog', 'cat') )

        # Ignore Case
        self.assertIsNone( re.search('dog', 'blah DoG blah') )
        self.assertEqual('DoG', re.search('dog', 'blah DoG blah', re.IGNORECASE).group())


        # findall() returns all as list
        # Notice I have removed the (groups)
        results = re.findall(r'[\w.]+@[\w.]+', 'blah blah ryan.bever@netapp.com blah blah foo@bar')
        self.assertEqual(['ryan.bever@netapp.com', 'foo@bar'], results)
        # If I leave the groups in the list is Tuples of the groups
        results = re.findall(r'([\w.]+)@([\w.]+)', 'blah blah ryan.bever@netapp.com blah blah foo@bar')
        self.assertEqual([('ryan.bever', 'netapp.com'), ('foo', 'bar')], results)
        # else empty list
        self.assertEqual([], re.findall(r'dog', 'cat') )


        # Here is a nice little idiom to just read an entire file and findall
        file1 = open('./file1.txt', 'rU')
        results = re.findall('line\d', file1.read())
        self.assertEqual(['line1', 'line2', 'line3'], results)
        file1.close()


    ##################################
    # Variable Scope
    ##################################

    def test_scope1(self):
        # globalVar is accessible
        self.assertEqual(1, globalVar1)

        # global var not changed if shadowed
        self.shadow_global_var()
        self.assertEqual(1, globalVar1)

    def shadow_global_var(self):
        # If you try to assign to it in a function - it is actually shadowed
        # see scope2
        globalVar1 = 2
        self.assertEqual(2, globalVar1)
        self.test_functions()


    ##################################
    # Modules
    ##################################

    def test_modules(self):
        # By convention this should go at the top of this module
        import example_module

        # Access function through module name
        result = example_module.fib(8)
        self.assertEqual([1, 1, 2, 3, 5, 8], result)

        # Or by assigning it to a local variable
        fib = example_module.fib
        self.assertEqual([1, 1, 2, 3, 5, 8], fib(8))

    def test_modules2(self):
        # Or import the names into the symbol table directly
        from example_module import fib

        self.assertEqual([1, 1, 2, 3, 5, 8], fib(8))


    ##################################
    # Try / Except
    ##################################

    def test_try(self):
        """
        The try ...except statement has an optional else clause, which, when present,
        must follow all except clauses.  It is useful for code that must be executed
        if the try clause does not raise an exception.
        The use of the else clause is better than adding additional code to the try
        clause because it avoids accidentally catching an exception that wasn't
        raised by the code being protected by the try...except statement.
        """

        try:
            f = open('noSuchFile.txt', 'rU')
        except FileNotFoundError as e:
            self.assertIsInstance(e, FileNotFoundError)
        else:
            f.close()
            self.fail('Expected FileNotFoundError')
            # finally:
            # Do finally actions here...

        # If an exception has arguments, they are printed as the last part
        # ('detail') of the message for unhandled exceptions.
        try:
            raise MyException('Exception Message', 'you can also add arbitrary arguments', ['list', 'of', 'stuff'])
        except MyException as e:
            self.assertIsInstance(e, MyException)
            self.assertEquals(
                ('Exception Message', 'you can also add arbitrary arguments', ['list', 'of', 'stuff']),
                e.args)
        else:
            self.fail('Expected MyException')



    ##################################
    # Generators / Generator expressions
    ##################################

    def test_generators(self):
        """
        Generators are a simple and powerful tool for creating iterators.
        They are written like regular functions but use the yield statement
        whenever they want to return data. Each time next() is called on it,
        the generator resumes where it left off
        (it remembers all the data values and which statement was last executed).
        """

        # This returns an iterator...
        def reverse(data):
            for index in range(len(data) - 1, -1, -1):
                yield data[index]

        s = ''
        for char in reverse('golf'):
            s += char
        self.assertEqual('flog', s)

    def test_generator_expression(self):
        """
        Some simple generators can be coded succinctly as expressions using a syntax
        similar to list comprehensions but with parentheses instead of brackets.
        These expressions are designed for situations where the generator is used
        right away by an enclosing function. Generator expressions are more compact
        but less versatile than full generator definitions and tend to be more memory
        friendly than equivalent list comprehensions.
        """

        # sum of squares
        result = 0
        for a_square in (i * i for i in range(10)):
            result += a_square
        self.assertEqual(285, result)

        # Or more compactly - using sum() function - which takes an iterable
        result = sum(i * i for i in range(10))
        self.assertEqual(285, result)


    ##################################
    # Classes
    ##################################

    def test_classes(self):
        class Dog:
            """Dog class ..."""

            kind = 'canine'
            """class variable shared by ALL instances"""

            def __init__(self, name):
                self.name = name
                """instance variable"""

                self.tricks = []
                """Correct use of instance variable"""

            def do_trick(self):
                if not self.tricks:
                    return "Sorry, I don't know any :("
                return random.choice(self.tricks)

        with self.assertRaises(TypeError):
            Dog()

        d1 = Dog('Fido')
        d2 = Dog('Buddy')

        self.assertEqual('canine', d1.kind)
        self.assertEqual('canine', d2.kind)

        self.assertEqual('Fido', d1.name)
        self.assertEqual('Buddy', d2.name)

        d1.tricks.append('roll-over')
        d1.tricks.append('fetch')

        self.assertEqual(['roll-over', 'fetch'], d1.tricks)
        self.assertEqual([], d2.tricks)

        self.assertNotEqual("Sorry, I don't know any :(", d1.do_trick())
        self.assertEqual("Sorry, I don't know any :(", d2.do_trick())

    def test_classes_private_attributes(self):
        """ "Private" instance variables that cannot be accessed except from inside an object don't exist in Python.

        However, there is a convention that is followed by most Python code:
        a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API
        (whether it is a function, a method or a data member).
        It should be considered an implementation detail and subject to change without notice.
        """
        class Dog:
            def __init__(self, name):
                self.name = name
                """instance variable"""

                self._tricks = []
                """ 'Private' - By Convention"""

            def add_trick(self, trick):
                self._tricks.append(trick)

            def do_trick(self):
                if not self._tricks:
                    return "Sorry, I don't know any :("
                return self._random_trick()

            def _random_trick(self):
                """ 'Private' - By Convention"""
                return random.choice(self._tricks)

        d1 = Dog('Fido')

        self.assertEqual("Sorry, I don't know any :(", d1.do_trick())
        d1.add_trick('fetch')
        self.assertNotEqual("Sorry, I don't know any :(", d1.do_trick())

        # Though you can still do this - Don't
        d1._tricks.append('sit')
        self.assertEqual(['fetch', 'sit'], d1._tricks)

    def test_classes_class_variables(self):
        """
        Shared data can have possibly surprising effects with involving
        MUTABLE OBJECTS
        such as lists and dictionaries.

        For example, the bad_tricks list in the following code should not be used
        as a class variable because just a single list would be shared by all Dog instances:
        """

        class Dog:
            """Dog class ..."""

            kind = 'canine'
            """class variable shared by ALL instances"""

            total_dog_count = 10
            """class variable shared by ALL instances"""

            bad_tricks = []
            """MISTAKE: mistaken use of class variable"""

            def __init__(self, name):
                self.name = name
                """instance variable"""

        d1 = Dog('Fido')
        d2 = Dog('Buddy')

        ####
        # Simple example
        ####
        d1.kind = 'Bulldog'
        self.assertEqual('canine', Dog.kind)
        self.assertEqual('Bulldog', d1.kind)
        self.assertEqual('canine', d2.kind)

        ####
        # More complicated example
        ####
        # This part is as expected
        Dog.total_dog_count += 1
        Dog.total_dog_count += 1
        Dog.total_dog_count += 1
        self.assertEqual(13, Dog.total_dog_count)
        self.assertEqual(13, d1.total_dog_count)
        self.assertEqual(13, d2.total_dog_count)

        # If accessed through an instance the value is copied to d1.total_doc_count
        d1.total_dog_count += 1
        self.assertEqual(13, Dog.total_dog_count)
        self.assertEqual(14, d1.total_dog_count)
        self.assertEqual(13, d2.total_dog_count)

        # Update class variable
        Dog.total_dog_count += 1
        Dog.total_dog_count += 1
        self.assertEqual(15, Dog.total_dog_count)
        self.assertEqual(14, d1.total_dog_count)    # d1.total_dog_count not updated as it's now a separate copy
        self.assertEqual(15, d2.total_dog_count)

        # delete the copied local instance of d1.total_dog_count then it will use the class variable again
        del d1.total_dog_count
        self.assertEqual(15, Dog.total_dog_count)
        self.assertEqual(15, d1.total_dog_count)    # d1.total_dog_count now class variable again
        self.assertEqual(15, d2.total_dog_count)


        ####
        # Mutable Type example
        ####
        d1.bad_tricks.append('sit')
        d2.bad_tricks.append('play-dead')
        self.assertEqual(['sit', 'play-dead'], d1.bad_tricks)
        self.assertEqual(['sit', 'play-dead'], d2.bad_tricks)

        Dog.bad_tricks.append('down')
        self.assertEqual(['sit', 'play-dead', 'down'], Dog.bad_tricks)
        self.assertEqual(['sit', 'play-dead', 'down'], Dog('new dog').bad_tricks)
        self.assertEqual(['sit', 'play-dead', 'down'], d1.bad_tricks)
        self.assertEqual(['sit', 'play-dead', 'down'], d2.bad_tricks)

    def test_classes_data_method_attribute_collision(self):
        """
        Data attributes override method attributes with the same name.

        To avoid accidental name conflicts, which may cause hard-to-find bugs in large programs,
        it is wise to use some kind of convention that minimizes the chance of conflicts.
        """
        class Dog:
            def __init__(self, name):
                self.name = name

            def name(self):
                return 'My name is: ' + self.name

        d1 = Dog('Fido')

        self.assertEqual('Fido', d1.name)
        with self.assertRaises(TypeError):
            d1.name()


    ##################################
    # Functions
    ##################################

    def test_functions(self):
        """The first line should always be a short, concise summary of the object's purpose.

        For brevity, it should not explicitly state the object's name or type,
        since these are available by other means (except if the name happens to be a
        verb describing a function's operation).
        This line should begin with a capital letter and end with a period.

        If there are more lines in the documentation string, the second line should be blank,
        visually separating the summary from the rest of the description. The following lines
        should be one or more paragraphs describing the object's calling conventions, its side effects, etc.

        The Python parser does not strip indentation from multi-line string literals in Python,
        so tools that process documentation have to strip indentation if desired.
        This is done using the following convention. The first non-blank line after the first line of
        the string determines the amount of indentation for the entire documentation string.
        (We can't use the first line since it is generally adjacent to the string's opening quotes
        so its indentation is not apparent in the string literal.) Whitespace "equivalent" to this
        indentation is then stripped from the start of all lines of the string. Lines that are indented
        less should not occur, but if they occur all their leading whitespace should be stripped.
        Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).

        :return: None
        """

        # functions can be assigned to variables
        my_fun1 = fun1
        self.assertEqual(1, my_fun1())

        # Keyword arguments allow for optional parameters
        self.assertEqual('req', fun2('req'))
        # Positional
        self.assertEqual('my_optional', fun2('req', 'my_optional', True))
        # Or named
        self.assertEqual('my_optional', fun2('req', optional='my_optional', use_optional=True))
        # Order can be changed when named
        self.assertEqual('my_optional', fun2('req', use_optional=True, optional='my_optional'))
        # Or optional parameters can be omitted
        self.assertEqual('opt', fun2('req', use_optional=True))

        # Arbitrary argument lists - similar to varargs
        joined = my_join(' ', 'word1', 'word2', 'word3')
        self.assertEqual('word1 word2 word3 ', joined)

        # This is different than java - can't pass an array to varargs
        with self.assertRaises(TypeError):
            joined = my_join(' ', ['word1', 'word2', 'word3'])
            self.assertEqual('word1 word2 word3 ', joined)
        # But you can unpack it like so:
        joined = my_join(' ', *['word1', 'word2', 'word3'])
        self.assertEqual('word1 word2 word3 ', joined)

        # ** gets a dictionary of the key/value arguments
        found = search('This text contains: key1:val1 key2:val2 key3:val3', key1='val1', key2='not_val2')
        self.assertEqual([('key1', 'val1')], found)

        # Wouldn't normally access annotations
        annotations = annotated_functions.__annotations__
        self.assertEqual(str, annotations['text'])
        self.assertEqual(float, annotations['f'])
        self.assertEqual(int, annotations['i'])
        self.assertEqual(TestExample, annotations['test_class'])
        self.assertEqual(str, annotations['return'])

    def test_functions_(self):
        """ Call by Value - where value is the object reference.

        The actual parameters (arguments) to a function call are introduced in the local symbol table of the
        called function when it is called; thus, arguments are passed using call by value
        (where the value is always an object reference, not the value of the object). When a function calls another function, a new local symbol table is created for that call.

        Actually, call by object reference would be a better description, since if a mutable object is passed,
        the caller will see any changes the callee makes to it (items inserted into a list).
        """
        a = 1
        b = 2
        swap(a, b)
        self.assertEqual(1, a)
        self.assertEqual(2, b)


def fun1():
    return 1


def fun2(required, optional='opt', use_optional=False):
    if use_optional:
        return optional
    return required


def my_join(separator, *strings):
    # Note next line would be a more pythonic choice here, but this is just an example
    # separator.join(strings)
    joined = ''
    for s in strings:
        joined += s + separator
    return joined


def search(text, **keyvals):
    # Note this example is a little contrived
    found = []
    for kv in keyvals.items():
        if kv[0] + ':' + kv[1] in text:
            # Note: next line adds tuple as two separate list items - so use append instead
            # found += kv
            found.append(kv)
    return found


def annotated_functions(text: str, i: int, f: float, test_class: TestExample = None) -> str:
    return text + str(i) + str(f) + str(test_class)


def swap(a, b):
    """Like Java this doesn't work."""
    temp = a
    a = b
    b = temp


def doc_test_example(a, b):
    """
    | If a docString contains a python REPL output like below it can be tested with doctest:
    | ``$ python3.5 -m doctest -v example.py``


    >>> doc_test_example(1, 2)
    1
    2

    :param a: Will be printed first
    :param b: Will be printed second
    :return: None
    """

    print(a)
    print(b)


class MyException(Exception):
    """Exception for testing example exceptions."""
    pass


# Boilerplate for running unit test when this script is called
# With more verbose output
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExample)
    unittest.TextTestRunner(verbosity=2).run(suite)
