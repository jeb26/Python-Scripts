from sys import argv

script, filename = argv

print "we're going to erase %r" % filename
print "If you don't want, hit ctrl-c (^C)."
print "If you do want tha, hit RETURN."

raw_input("?")

print "Opening file...."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("> ")
line2 = raw_input("> ")
line3 = raw_input("> ")

print "Writing to file...."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing file. Operations complete......"
target.close()


