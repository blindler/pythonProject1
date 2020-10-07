import math

# asking for user input
length = float(input("Enter the Length of the Room: "))
width = float(input("Enter the Width of the Room: "))
height = float(input("Enter the Height of the Room: "))
numDoors = float(input("Enter the Number of Doors: "))
numWindows = float(input("Enter the Number of Windows: "))

# Calculation for surface Area not accounting for windows and doors
surfaceArea = (2 * (width * height)) + (2 * (length * height))

# Subtracting the window and door area from the total surface area
surfaceArea -= (numDoors * 20)
surfaceArea -= (numWindows * 15)

# multiplying surface area by 1.1 to get that 10% extra paint accounted for
paintArea = surfaceArea * 1.1

# NumGallons is calculated as an exact float
numGallons = paintArea/350

# rounding the number of gallons up one, since you cannot buy a fraction of a gallon
#numGallons += 0.99
numGallons = math.ceil(numGallons)
#numGallons = int(numGallons)

# printing final answer
print("\nThe surface Area of the room minus the doors and windows is " + str(surfaceArea) + " Square feet. One gallon of paint covers 350 square feet, so you will need " + str(numGallons) + " gallons of paint to cover the room with 10% extra paint.")

answer = "The surface Area of the room minus the doors and windows is %s Square feet. One gallon of paint covers 350 square feet, so you will need %s gallons of paint to cover the room with 10 extra paint." %(surfaceArea, numGallons)

print( answer )

print("\nThe surface Area of the room minus the doors and windows is {0} Square feet. One gallon of paint covers 350 square feet, so you will need {1} gallons of paint to cover the room with 10% extra paint.".format(surfaceArea,numGallons) )

answer = f'The surface Area of the room minus the doors and windows is {surfaceArea} Square feet. One gallon of paint covers 350 square feet, so you will need {numGallons} gallons of paint to cover the room with 10% extra paint.'

print(answer)
