# Code for the Entrance Hall scene
#   This is where the player starts the game
#   All of our scenes are in separate files, b/c that keeps the size manageable
#
#  There are active TODO in this file

from scene import Scene

class EntranceHall(Scene):
	def __init__(self):
		self.description_power = """
The ornate marble entrance hall towers into a vaulted ceiling.
Light splays across the surfaces, illuminating Impressionist
paintings and modern sculptures. The sounds of the party
are faintly muffled here, but the hum of conversation is steady.

The doorman stands at the door to the entrance, greeting a
seemingly endless stream of guests who flow into the ballroom.
A set of stairs leads to the second floor.
The door to the billiard room stands opposite the ballroom.
"""
		self.description_no_power = """
The ornate marble entrance hall towers into a vaulted ceiling.
A lone streetlight shines through the window but does little
to illuminate the room. Guests are checking their phones and
conversing. The doorman is on the phone, presumably to the power
company. 

The double doors lead outside.
There are stairs here, leading to the second floor.
The ballroom is through the east door.
The billiard room lies through the west door.
"""
	def start(self, game_objects):
		if game_objects["power"] == True:
			print self.description_power
			while True:
				inp = self.action_menu()
#"Go   Steal   Pick Lock   Use   Sap   Look   Wait   Menu" 
				if inp == "go":
					result = self.go(game_objects)
					if result != "cancel":
						return result
				elif inp == "steal":
					# the power is on and you tried to steal!
					print "Steal with power = game over" # TODO - rewrite this description
					return "game_over"
				elif inp == "pick lock":
					print "No locks to pick."
				elif inp == "use":
					print "There's nothing to use here."
				elif inp == "sap":
					print "Sap w/multiple people in room = game over" # TODO - rewrite this description
					return "game_over"
				elif inp == "wait":
					print "You loiter in the room, ostensibly admiring the art."
					return "wait"
				elif inp == "menu":
					return "pause"
				elif inp == "look":
					print self.description_power
				else:
					print "I'm not sure what you meant by that."
		elif game_objects["power"] == False:
			print self.description_no_power
			while True:
				inp = self.action_menu()
#"Go   Steal   Pick Lock   Use   Sap   Look   Wait   Menu" 
				if inp == "go":
					result = self.go(game_objects)
					if result != "cancel":
						return result
				elif inp == "steal":
					# the power is on and you tried to steal!
					print "Steal without power, you did it!" # TODO - rewrite this description and return a value for Map to successfully update params
				elif inp == "pick lock":
					print "No locks to pick."
				elif inp == "use":
					print "There's nothing to use here."
				elif inp == "sap":
					print "Sap while it's dark? Sure, whatever." # TODO - rewrite this description and return a value for Map to successfully update params
				elif inp == "wait":
					print "You hang about in the darkened room, blending in with the crowd."
					return "wait"
				elif inp == "menu":
					return "pause"
				elif inp == "look":
					print self.description_no_power
				else:
					print "I'm not sure what you meant by that."
