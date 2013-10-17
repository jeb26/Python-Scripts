cities = {'NY':'Albany','NJ':'Trenton','PA':'Harrisburg'}

def find_city(dictionary,searchTerm):
    if searchTerm in dictionary:
        print dictionary[searchTerm]
    else:
        print "was not found."

cities['_find'] = find_city

while True:
    print "Please enter a State: ",
    userInput = raw_input("> ")
    if not userInput: break

    city = cities['_find'](cities, userInput)
