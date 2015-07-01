from scene import Scene

class UpstairsLanding(Scene):
	def __init__(self):
		self.description_power = """
The upstairs landing shines, light playing off the marble
surfaces of the floor, wall and stairs. The stone bust
of a gargoyle leers at you.

If not for the gleeful sounds of the party drifting up
from below, this would be the creepiest place ever.

The bedrooms lie to the east, bathed in shadows.
The library lies to the west.
The stairs leading down to the entrance hall are here.
"""
		self.description_no_power = """
This upstairs landing got a lot creepier without power.
The gargoyle bust casts strange shadows along the wall,
and as you creep along the wall you cannot shake the 
notion that it may be moving occasionally.

Best to move on.

The power is out; shadows permeate the rooms.

The bedrooms lie to the east.
The library lies to the west.
The stairs leading down to the entrance hall are here.
"""
	def start(self, game_objects):
		if game_objects["power"] == True:
			print self.description_power
			# TODO: guard logic here
			while True:
				inp = self.action_menu()
#"Go   Steal   Pick Lock   Use   Sap   Look   Wait   Menu" 
				if inp == "go":
					result = self.go(game_objects)
					if result != "cancel":
						return result
				elif inp == "steal":
					# the power is on and you tried to steal!
					print """
No longer able to resist the siren call of the gargoyle
statue, you try to pry it from the walls.

You are still tugging at the stone base when law
enforcement arrives to ruin your day.

You are arrested!
""" # This is why you don't steal things while the lights are on.
					return "game_over"
				elif inp == "pick lock":
					print "No locks to pick."
				elif inp == "use":
					print "There's nothing to use here."
				elif inp == "sap":
					print " This hasn't been implemented because guard logic doesn't exist yet." #TODO
					return "game_over"
				elif inp == "wait":
					print "You loiter in the room, ostensibly admiring the art."
					print "There might need to be guard logic here." #TODO
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
					# the power is off, you can do it!
					print """
You can't fit the stone gargoyle in your pockets,
or even under the folds of your cloak.

Undaunted, you steal a pack of gum from one of 
the upstairs guards. Life without power is so liberating.
"""
					return "wait" # to increment the clock
				elif inp == "pick lock":
					print "No locks to pick."
				elif inp == "use":
					print "There's nothing to use here."
				elif inp == "sap":
					print """
You knock out a guard.
What a senseless use of violence.
"""  #TODO : guard logic should go here
					return "wait"
				elif inp == "wait":
					print "You hang about in the darkened room, blending in with the crowd."
					return "wait"
				elif inp == "menu":
					return "pause"
				elif inp == "look":
					print self.description_no_power
				else:
					print "I'm not sure what you meant by that."
