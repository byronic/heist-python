from scene import Scene

# TODO: fix the spacing on the two-guard game over on sap

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
		# self.guards[] has descriptions for 0 guards, 1 guard, and 2 guards in this room
		self.guards = [ "", "A lone guard patrols here.", "Two guards scan the area as they walk." ]
	def start(self, game_objects):
		if game_objects["power"] == True:
			print self.description_power
			print self.guards[game_objects['guards']]
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
					if game_objects['guards'] == 1:
						print "You handily knock out the guard and drag him behind the stone bust."
						return "sap"
					elif game_objects['guards'] > 1:
						print "You have just enough time to punch out one guard before the other draws a gun. Oh dear."
						print "The gun barrel jams roughly at the base of your neck. You raise your hands in the air."
						return "game_over"
					else:
						print "You look about for someone to take your rage out on."
						print "Sadly, you are alone."
				elif inp == "wait":
					print "You loiter in the room, ostensibly admiring the art."
					if game_objects['guards'] > 0:
						print "A guard eyes you suspiciously. Sweating, you continue"
						print "to admire the art -- to no avail! You are recognized."
						print "The guard snaps your hands into a pair of cuffs."
						print "\nAh, the perils of infamy."
						return "game_over"
					return "wait"
				elif inp == "menu":
					return "pause"
				elif inp == "look":
					print self.description_power
					print self.guards[game_objects['guards']]
				else:
					print "I'm not sure what you meant by that."
		elif game_objects["power"] == False:
			print self.description_no_power
			print self.guards[game_objects['guards']]
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
					if game_objects['guards'] == 1:
						print "You handily knock out the guard and drag him behind the stone bust."
						return "sap"
					elif game_objects['guards'] > 1:
						print "You have just enough time to punch out one guard before the other draws a gun. Oh dear."
						print "The gun barrel jams roughly at the base of your neck. You raise your hands in the air."
						return "game_over"
					else:
						print "You look about for someone to take your rage out on."
						print "Sadly, you are alone."
					return "wait"
				elif inp == "wait":
					print "You grip the staircase railing and blend into the shadows."
					return "wait"
				elif inp == "menu":
					return "pause"
				elif inp == "look":
					print self.description_no_power
					print self.guards[game_objects['guards']]
				else:
					print "I'm not sure what you meant by that."
