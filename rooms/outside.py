from scene import Scene

class Outside(Scene):
	def __init__(self):
		# the description for the out-of-doors is the same regardless
		#  of power being on or off.
		self.description = """
The lawn here is expansive and covered in fine art
and twisting stone pathways that wind through gardens.
The mansion itself has a fine view of the city,
its lights twinkling brightly in the far distance.
The double-doors leading inside stand open, and party
guests stream from the valet up the main path.
No chance of anyone recognizing you here... too dark,
and too many people. You permit yourself a small smile.
"""

	def start(self, game_objects):
		# if we left the house after completing the heist, the game is over
		if game_objects['heist complete'] == True:
			return "game_win"
		# otherwise, wander the gardens
		print self.description
		while True:
			inp = self.action_menu()
#"Go   Steal   Pick Lock   Use   Sap   Look   Wait   Menu" 
			if inp == "go":
				result = self.go(game_objects)
				if result != "cancel":
					return result
			elif inp == "steal":
				# there's nothing to steal in this room
				print """
The outside statues and fountains are made of cement,
and the hedges aren't interesting enough to take.
You decide against trying to steal any of them.
""" 
			elif inp == "pick lock":
				print """
The exterior double doors are already unlocked.
"""
			elif inp == "use":
				print "There's nothing to use here."
			elif inp == "sap":
				print """
With a brazen chuckle, you sneak up behind the doorman
and knock him out cold.
As this was done in full view of the party guests,
your protestations of innocence fool exactly no one.
"""
				return "game_over"
			elif inp == "wait":
				print """
You wander the grounds outside for awhile.
The night is tranquil and quiet, as the partiers 
are all inside.
Fresh air enlivens you, and you return from
meandering the gardens with a spring in your step.
"""
				return "wait"
			elif inp == "menu":
				return "pause"
			elif inp == "look":
				print self.description
			else:
				print "I'm not sure what you meant by that."

