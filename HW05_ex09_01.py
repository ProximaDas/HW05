#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
from sys import argv
# Body
def read_file():
	file_handler = open(argv[1])
	content = file_handler.read()
	word_list = content.split()
	for word in word_list:
		if len(word) > 20:
			print word

##############################################################################
def main():
    read_file() # Call your functions here.

if __name__ == '__main__':
    main()
