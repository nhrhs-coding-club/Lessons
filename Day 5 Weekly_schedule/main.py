
from scheduler import Weekly_Scheduler


def Main_Menu():
	print("Menu:")
	print("\t1. Print Schedule")
	print("\t2. Add Event")
	print("\t3. Remove Event")
	print("\t4. Exit")

	response = 10
	while response < 1 or response > 4:
		print("Please choose an option: ")
		response = input()

	return response

def Delete_Menu():
	print("Enter the title of the event to be deleted: ")
	return raw_input()

def Add_Menu():
	print("Enter all of the information:")
	title = raw_input("Title: ")
	description = raw_input("Description: ")
	day = raw_input("Day: ")
	start_time = raw_input("Start time: ")
	end_time = raw_input("End time: ")

	return {'title' : title,
				'description' : description,
				'day' : day,
				'start_time' : start_time, 
				'end_time' : end_time }



ws = Weekly_Scheduler()

user_input = 0
while user_input != 4:
	user_input = Main_Menu()

	if user_input == 1:
		ws.Print()
	elif user_input == 2:
		ws.Add_Event(Add_Menu())
	elif user_input == 3:
		ws.Delete_Event(Delete_Menu())
	else:
		pass

print("Thank you for using the Weekly Scheduler.")







