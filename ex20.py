#imports from the system module the arg vector module
from sys import argv

##unpacks the arg vector
script, input_file = argv

#defines a function to print all the contents a file via the read
#method
def print_all(f):
	print f.read()
	
#returns the files read postion to the beginning of the file
#to re-read file	
def rewind(f):
	f.seek(0);


def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
