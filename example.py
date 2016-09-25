#!/usr/bin/python -tt

"""-tt tells python to stop if there is mixed tabs and spaces in the file"""

import unittest

class TestPythonBasics(unittest.TestCase):

    def test_Wtf(self):
        """self instead of this"""
        """No block comments"""
        return


    ##################################
    # Strings
    ##################################
    def test_Strings(self):

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

        # String cat with + operator
        s = 'word1' + ' ' + 'word2'
        self.assertEqual('word1 word2', s)

        # Unlike Java you can't cat a string an int
        with self.assertRaises(TypeError):
            'word1' + 3
        self.assertEqual('word13', 'word1' + str(3))

    def test_Strings_split(self):

        #split() with no arg splits on white
        l = 'This is a string\twith\n\n\twhite'.split()
        self.assertEqual( ['This', 'is', 'a', 'string', 'with', 'white'], l)


    def test_Strings_slice(self):

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

        # The other feature is that start or end may be a negative number, which means it counts from the end of the String instead of the beginning. So:
        # s[-1]    # last character in the String
        # s[-2:]   # last two substring in the String
        # s[:-2]   # everything except the last two substring
        self.assertEqual('e', s[-4])
        self.assertEqual('lo', s[-2:])
        self.assertEqual('Hel', s[:-2])

        # Python is kind to the programmer if there are fewer characters than you ask for. 
        # For example, if you ask for a[:-2] and a only contains one character, you get an empty String instead of an error. 
        # Sometimes you would prefer the error, so you have to be aware that this may happen.
        self.assertEqual('ello', s[1:99])
        self.assertEqual('Hello', s[-99:])
        self.assertEqual('', s[:-99])


        # Also can be important that [:] returns a shallow copy of a list. it means that every slice notation returns a list which have new address in memory, 
        # but its elements would have same addresses that elements of source list have.






    ##################################
    # Lists
    ##################################
    def test_Lists(self):
        # References to lists are pointers
        a = [1, 2, 3]
        b = a
        self.assertEqual([1, 2, 3], a)
        self.assertEqual([1, 2, 3], b)

        # Changes made to a are reflected in b
        a[0] = 0;
        a.append(4)
        self.assertEqual([0, 2, 3, 4], a)
        self.assertEqual([0, 2, 3, 4], b)

        # Use "in" keyword to test
        a = [1, 2, 3]
        self.assertTrue( 1 in a )
        self.assertFalse( 4 in a )

    def test_Lists_copy(self):
        # to (shallow) copy the array use slice
        a = [1, 2, 3]
        b = a[:]
        self.assertEqual([1, 2, 3], a)
        self.assertEqual([1, 2, 3], b)

        # Changes made to a are NOT reflected in b
        # Note if these were objects changes to the object would be reflected in b
        a[0] = 0;
        a.append(4)
        self.assertEqual([0, 2, 3, 4], a)
        self.assertEqual([1, 2, 3], b)

    def test_Lists_slice(self):
        # a[start:end] # items start through end-1
        # a[start:]    # items start through the rest of the array
        # a[:end]      # items from the beginning through end-1
        # a[:]         # a copy of the whole array
        # a[start:end:step] # start through not past end, by step
        # The key point to remember is that the :end value represents the first value that is NOT in the selected slice. 
        s = 'Hello'
        self.assertEqual('el', s[1:3])
        self.assertEqual('ello', s[1:])
        self.assertEqual('Hel', s[:3])
        self.assertEqual('Hello', s[:])
        self.assertEqual('Hlo', s[::2])

        # The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:
        # a[-1]    # last item in the array
        # a[-2:]   # last two items in the array
        # a[:-2]   # everything except the last two items
        self.assertEqual('e', s[-4])
        self.assertEqual('lo', s[-2:])
        self.assertEqual('Hel', s[:-2])

        # Python is kind to the programmer if there are fewer items than you ask for. 
        # For example, if you ask for a[:-2] and a only contains one element, you get an empty list instead of an error. 
        # Sometimes you would prefer the error, so you have to be aware that this may happen.
        self.assertEqual('ello', s[1:99])
        self.assertEqual('Hello', s[-99:])


        # Also can be important that [:] returns a shallow copy of a list. it means that every slice notation returns a list which have new address in memory, 
        # but its elements would have same addresses that elements of source list have.


    def test_Lists_append_extend(self):
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


    def test_Lists_pop(self):
        l = [1, 2, 3]
        item = l.pop()
        self.assertEqual(3, item)
        self.assertEqual([1, 2], l)

        l = [1, 2, 3, 4]
        item = l.pop(1)
        self.assertEqual(2, item)
        self.assertEqual([1, 3, 4], l)

    def test_Lists_sorted(self):
        # sorted returns a new list and l is unchanged
        l = [5, 2, 3, 1, 4]
        sl = sorted(l)
        self.assertEqual([1, 2, 3, 4, 5], sl)
        self.assertEqual([5, 2, 3, 1, 4], l)

        # Default sort is the natural sort
        # But you can use a custom key - Which is not a traditional comparator
        # but instead returns a shadow list that is then used to sort
        # so we can sort on the len() function which on takes a single parameter
        l = [ 'dd', 'z', 'aaa', 'bbb', 'cc']
        sl = sorted(l, key=len)
        self.assertEqual( [ 'z', 'dd', 'cc', 'aaa', 'bbb'] , sl)

        # Notice this also demonstrates that the sorted method is stable



    ##################################
    # Tuples
    ##################################
    def test_Tuples(self):

        #tuples are defined with ()
        t = (1, 2, 3)

        # Access with []
        self.assertEqual(1, t[0]) 

        # Tuples are immutable
        with self.assertRaises(TypeError):
            t[0] = 0
                
        # Tuple assignment - not extremely common
        (x, y) = (1, 2)
        self.assertEqual(1, x) 
        self.assertEqual(2, y) 


    ##################################
    # Dictionaries
    ##################################
    def test_Dictionaries(self):

        # dictionaries are defined with {}
        d = {}

        # You can Access with []
        d['key1'] = 'val1'
        d['key2'] = 'val2'
        d['key3'] = 'val3'
        self.assertEqual('val1', d['key1'])

        # But Accessing a non-existent key is an error
        with self.assertRaises(KeyError):
            x = d['noSuchKey']

        # There is a .get method that will retrun the value or None
        self.assertEqual('val1', d.get('key1'))
        self.assertIsNone(d.get('noSuchKey'))

        # Use "in" keyword to test
        self.assertTrue( 'key1' in d )
        self.assertFalse( 'noSuchKey' in d )

        # keys / values
        self.assertEqual( ['key1', 'key2', 'key3'], sorted( d.keys() ) ) # sorted needed because order is not guaranteed
        self.assertEqual( ['val1', 'val2', 'val3'], sorted( d.values() ) ) # sorted needed because order is not guaranteed

        # items - returns key/value as a tuple
        # sorted needed because order is not guaranteed
        self.assertEqual( [ ('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3') ], sorted( d.items() ) ) 


    ##################################
    # Read/Write files
    ##################################
    def test_Read_Write_Files(self):

        # Open for reading U with universal line endings i.e. \n or \r or \r\n
        file1 = open('./file1.txt', 'rU')

        # This will read the file line by line
        s = ''
        for line in file1:
            s += line
        file1.close()
        self.assertEqual('line1\nline2\nline3 word2\n', s)

        # This will read all lines into a list
        file1 = open('./file1.txt', 'rU')
        lines = file1.readlines()
        file1.close()
        # Notice newlines are still there
        self.assertEqual( ['line1\n', 'line2\n', 'line3 word2\n'], lines)

        # This will read the entire file into a String
        file1 = open('./file1.txt', 'rU')
        s = file1.read()
        file1.close()
        self.assertEqual('line1\nline2\nline3 word2\n', s)



# Boilerplate for running unit test when this script is called
# With more verbose output
suite = unittest.TestLoader().loadTestsFromTestCase(TestPythonBasics)
unittest.TextTestRunner(verbosity=2).run(suite)
