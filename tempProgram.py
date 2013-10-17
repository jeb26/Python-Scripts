##Function that takes in 3 parameters a starting temperature, and ending temperature
##and a step size. The function prints a table from start to end increasing by the step
##size. Program MUST perform input validation NO TEMPS LESS THAN A CONSTANT LOWER LIMIT
##NO TEMPS HIGHER THAN A CONSTANT HIGHER LIMIT, and, NO STEP SIZE GREATER THAN THE
##DIFFERENCE BETWEEN THE START TEMP AND THE END TEMP.

def tempConverter():
    MIN_TEMP = 0
    MAX_TEMP = 50000

    userTempMin = int(input("Please enter a minimum temperature in celsius: "))

    while userTempMin < MIN_TEMP:
        print("The temperature you entered is too small. Please try",
              " again: ")
        userTempMin = int(input())

    print("Please enter a maximum temperature that is less than 50K: ")
    userTempMax = int(input())

    while userTempMax < MIN_TEMP or userTempMax > MAX_TEMP:
        print("The temperature you entered is not within the interval of",
              " (Min < userTemp < Max). Please enter new temperature: ")
        userTempMax = int(input())

    validStepSize = userTempMax - userTempMin

    userStep = int(input("Please enter a step size: "))

    while userStep >= validStepSize:
        print("The number that you have entered is too large please decrease: ")
        userStep = int(input())

    for i in range(userTempMin,userTempMax,userStep):
        degreeC = i
        degreeF = ((9/5) * degreeC) + 32
        print("Celsius \t\t Farenheit")
        print("---------------------------------")
        print(degreeC," \t\t\t ",degreeF,"\n")
        
        
