import pprint

pp = pprint.PrettyPrinter(indent=4)

class Event(object):

	def __init__(self, title, description, start_time, end_time):
		self.title = title
		self.description = description
		self.start_time = start_time
		self.end_time = end_time





class Weekly_Scheduler(object):

	def __init__(self):
		self.schedule = {
			"monday" : [],
			"tuesday" : [],
			"wednesday" : [],
			"thursday" : [],
			"friday" : [],
			"saturday" : [],
			"sunday" : []
		}
	

	def Print(self):
		
		# Sunday
		print("\n----------------------------------------------")
		print("\nSunday:")
		for event in self.schedule["sunday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\nMonday:")
		for event in self.schedule["monday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\nTuesday:")
		for event in self.schedule["tuesday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\nWednesday:")
		for event in self.schedule["wednesday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\nThursday:")
		for event in self.schedule["thursday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\nFriday:")
		for event in self.schedule["friday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\nSaturday:")
		for event in self.schedule["saturday"]:
			print("\t" + event.title + " - " + event.start_time)
			print("\t" + event.description)
			print("")

		print("\n----------------------------------------------\n")


	def Add_Event(self, data):

		try:
			self.schedule[ data["day"].lower() ].append(Event(data["title"], 
				data["description"],
				data["start_time"],
				data["end_time"]))

		except Exception as e:
			print(str(e))
			print("Invalid input for adding an event.")


	def Delete_Event(self, title):
		pass
