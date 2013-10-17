##Write a prog that prompts for a number of students. then each name and score and
##then displays the name of student with highest score.

scoreAcc = 0
nameAcc = None
currentScore = 0
currentName = None

numRuns = int(input("Please enter the number of students: "))

for i in range(numRuns):
    currentName = str(input("Please enter the name of the current student: "))
    currentScore = int(input("Pleae enter the score the current student: "))

    if currentScore > scoreAcc:
        scoreAcc = currentScore
        nameAcc = currentName

print("The highest scoring student is: ",nameAcc)

    
