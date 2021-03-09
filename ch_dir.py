#!/usr/bin/python

import os


inputin		= raw_input("Enter a path: ")
os.chdir(inputin)
print "Current path: ", os.getcwd()
