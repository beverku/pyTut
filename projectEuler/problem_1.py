"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


##############################
# Here is my first solution
##############################
def is_multiple(i):
    return i % 3 == 0 or i % 5 == 0


# Answer is: 233168
def main():
    _sum = 0
    for i in range(1000):
        if is_multiple(i):
            _sum += i
    print(_sum)
##############################
# End Here is my first solution
##############################


##############################
# This is probably a more pythonic answer using
# list comprehension and filter
##############################
def answer2():
    _sum = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print(_sum)


##############################
# Probably even better with a generator expression
##############################
def answer3():
    _sum = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    print(_sum)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
    answer2()
    answer3()
