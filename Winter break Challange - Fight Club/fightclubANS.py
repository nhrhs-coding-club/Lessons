
# IMPORTS
import random
import time


########################  OBJECT DEFINITIONS ########################

class Hero(object):

	# Static variable
	#   This means it applies to all Goblin instances
	attacks = {
		"slash" : 100,
		"stab" : 190,
		"insult" : 30,
		"triple ultimate super sword blast" : 300
	}

	"""
		__init__ is called when you construct an instance of the Goblin class

		Do all of the work necessary to make a goblin here,
			such as create instance variables

	"""
	def __init__(self, name, health, gold, xp, drops=[]):
		print("A Hero of myth has been born.")

		# Instance variables
		self.name = name
		self.health = health
		self.gold = gold
		self.xp = xp
		self.drops = drops

		# Start the hero as living
		self.isAlive = True	

	"""
		Choose a random attack.  

		If the player is dead, don't attack -- that's impossible.

		Returns the attack name the amount of damage that it does.  

	"""
	def Attack(self):
		if self.isAlive:
			choice = random.choice(Hero.attacks.keys())
			return (choice, Hero.attacks[choice])
		else:
			return None

	"""
		Simulate taking damage.

		Simply subtract the damage from the player's health.
		If the health drops below zero, make the player dead.

	"""
	def TakeDamage(self, damage):
		self.health -= damage
		if self.health < 0:
			self.isAlive = False



class Goblin(object):
	
	# Static variable
	#   This means it applies to all Goblin instances
	attacks = {
		"slash" : 100,
		"bash" : 110,
		"nibble" : 12
	}

	"""
		__init__ is called when you construct an instance of the Goblin class

		Do all of the work necessary to make a goblin here,
			such as create instance variables

	"""
	def __init__(self, name, health, gold, xp, drops=[]):
		print("An evil Goblin just spawned!")

		# Instance variables
		self.name = name
		self.health = health
		self.gold = gold
		self.xp = xp
		self.drops = drops

		# Start the goblin as living
		self.isAlive = True


	"""
		Choose a random attack.  

		If the player is dead, don't attack -- that's impossible.
		
		Returns the attack name the amount of damage that it does.  

	"""
	def Attack(self):
		if self.isAlive:
			choice = random.choice(Goblin.attacks.keys())
			return (choice, Goblin.attacks[choice])
		else:
			return None


	"""
		Simulate taking damage.

		Simply subtract the damage from the player's health.
		If the health drops below zero, make the player dead.

	"""
	def TakeDamage(self, damage):
		self.health -= damage
		if self.health < 0:
			self.isAlive = False




########################  MAIN PROGRAM ########################

"""
	OBJECTIVE
		Make the evil goblin and the hero fight to the death.  

		Specific areas that need code are marked with CODE

		DO NOT ALTER ANY GIVEN CODE


"""
print("----------------------------------------------------------------")
print("Welcome to the Arena\n")


evil_goblin = Goblin("Chad", 1000, 512, 256, drops=["sword", "shield"])
heroic_hero = Hero("Bjourne Bjorgisson", 1400, 500000, 
					1000000, drops=["potion", 
									"armor of winning",
									"mother's blanket",
									"pocket sand"])


# CODE
# 	Decide who attacks first
# 	Roll a die or something with the random library


# CODE
#	Print who is going first


print("")
print("Let the fight begin!")
print("")
while evil_goblin.isAlive and heroic_hero.isAlive:
	
	# CODE
	#	Have the two adversaries attack each other
	#	Make sure to handle getting None back from the Attack() method!
	#   Make sure to print every step!
	#	Optionally add a time.sleep(1) to pace the game
	#	Optionally print each player's health after an attack

	if heroic_hero.isAlive:
		attack, damage = heroic_hero.Attack()
		evil_goblin.TakeDamage(damage)
		print("\t" + evil_goblin.name + " takes " + str(damage) + " from the hero's " + attack + "!")
	else:
		continue
	time.sleep(1)
	if evil_goblin.isAlive:
		attack, damage = evil_goblin.Attack()
		heroic_hero.TakeDamage(damage)
		print("\t" + heroic_hero.name + " takes " + str(damage) + " from the goblin's " + attack + "!")
	else:
		continue
	time.sleep(1)

# CODE
#	Determine the winner
#	Announce who the winner is


print("\n")

winner, loser = (heroic_hero, evil_goblin) if heroic_hero.isAlive else (evil_goblin, heroic_hero)

print(winner.name + " is the winner!\n")

print(winner.name + " is awarded:")
print("\t+" + str(loser.xp) + " experience")
for drop in loser.drops:
	print("\t" + drop)

print("----------------------------------------------------------------")








