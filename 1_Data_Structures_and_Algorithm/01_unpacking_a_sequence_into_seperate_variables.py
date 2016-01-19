#!/usr/bin/python

"""
Unpack a N-element tuple or sequence into a collection of N variables
"""

print "*********************************\n"
# Tuple
p = (4, 5)
x, y = p
print "Value of Tuple p = {}".format(p)
print ("x = {}, y = {}".format(x, y))

print "*********************************\n"
# Sequence (List)
data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, data = data
print "Sequence data = {}".format(data)
print("name = {}, shares = {}, price = {}, data = {}".format(name, shares, price, data))

print "*********************************\n"
data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, month, date) = data
print("Further unpacking of the above sequence")
print('name = {0}, shares = {1}, price = {2}, year = {3}, month = {4}, date = {5}'.format(
        name, shares, price, year, month, date))

print "*********************************\n"
# String
S = 'hello'
a, b, c, d, e = S
print a, b, c, d, e

print "*********************************\n"
# To discard certain values using throwaway variables
data = ["ACME", 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
