print("This is the grade Calculator")
midtermOne = input("What is your first midterm grade? ")
midtermTwo = input("What is your second midterm grade? ")
midtermThree = input("What is your third midterm grade? ")
finals = input("What is your finals grade? ")
finalGrade = float(midtermOne) * 0.2 + float(midtermTwo) * 0.2 + float(midtermThree) * 0.2 + float(finals) * 0.4
print("Your final grade is: " + str(finalGrade))