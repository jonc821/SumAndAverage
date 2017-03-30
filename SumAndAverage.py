f = open("data.txt", "r")

fileContents = f.read().splitlines()

sum = 0

for number in fileContents:
	sum = sum + int(number)
	
print("The sum of the numbers is " + str(sum) + ".")

totalNumbers = 0

for number in fileContents:
	totalNumbers += 1
	
average = sum / totalNumbers

print("The average of the numbers is " + str(average) + ".")

