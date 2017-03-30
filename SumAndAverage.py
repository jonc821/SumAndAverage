f = open("data.txt", "r")

fileContents = f.read().splitlines()

sum = 0

for number in fileContents:
	sum = sum + int(number)
	
print("The sum of the numbers is " + str(sum)) + "."

