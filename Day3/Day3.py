

##############################################
#	ATM Program
#	
#	Nice.
##############################################

def PrintMenu():

	print("Menu:")
	print("\t1. Deposit")
	print("\t2. Withdraw")
	print("\t3. Check balance")
	print("\t4. Exit")

def GetResponse(prompt):
	try:
		response = input("Choose an option (1-4): ")
		return response
	except:
		print(prompt)
		return GetResponse("Choose an option (1-4): ")

def ValidateInput(response, lower_bound, upper_bound):
	if response > upper_bound or response < lower_bound:
		print("Invalid input.  Please enter a number 1-4.")
		return False
	return True

def Deposit(balance):
	response = GetResponse("Amount to add (0-10000): ")

	while not ValidateInput(response, 0, 10000):
		response = GetResponse("Amount to add (0-10000): ")

	balance += response


def Withdraw(balance):
	response = GetResponse("Amount to withdraw (1-" + str(balance) + "): ")
	while not ValidateInput(response, 1, balance):
		response = GetResponse("Amount to withdraw (1-" + str(balance) + "): ")	

	balance -= response


def CheckBalance(balance):
	print("Your balance is $" + str(balance) + " . Nice.")

def Run():
	print("\nRunning ATM program ...")
	print("----------------------------------")

	balance = 500.00

	while(True):
		PrintMenu()
		response = GetResponse("Invalid input.  Please enter a number 1-4.")

		while not ValidateInput(response, 0, 4):
			response = GetResponse("Invalid input.  Please enter a number 1-4.")

		if response == 1:
			Deposit(balance)
		elif response == 2:
			Withdraw(balance)
		elif response == 3:
			CheckBalance(balance)
		elif response == 4:
			break

		print("\n----------------------------------\n")

Run()








