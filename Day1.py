

# Python Demo

myList = [1, 2, 3, 'Blerp', "Derp"]
myDict = {'firstName' : 'Nate',
			'lastName' : 'Moon'}
print(myList[2])

"""
Challenge 1:
	Print this statement to console:
		Use 1 print statement and 
		ONLY the variable names
		myList and myDict

	Nate Moon 123 Blerp

	Integer -> String
		str(3) == "3"
		str(myList[0])

"""
"""
	x = 2

	Same thing:
	x = x + 1
	x += 1

"""
myDict['firstName'] += " "
myDict['lastName'] += " "
myList[2] = str(myList[2]) + " "

print(myDict['firstName'] + \
	 myDict['lastName'] + \
	 str(myList[0]) \
	 + str(myList[1]) \
	 + myList[2] \
	 + myList[3])



"""
Challenge 2:
	Make one variable with:
		Your name, age, and the names
		of 3 of your pets (make 3 up)
"""


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

nums = [i for i in range(0, 10)]
print(nums)

output = ""
for number in nums:
	output += str(number) + " "

print(output)












