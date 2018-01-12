#!/usr/bin/env python

#print "hello Python"

import sys

hello = 'hello'
python = 'Python'

print hello, python



name = sys.argv[1]

age = int(sys.argv[2])

diff = 100 - age



print 'Hello', name + ', you will be 100 in ', diff, 'years!'
