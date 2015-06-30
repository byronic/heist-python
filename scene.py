# TODO: Add the turn logic to the start function
# TODO: split this into files per scene to keep it simple (i.e. scene.py, entrancehall.py, etc.
# TODO: Turn stuff actually has to flip back into Map's logic; so map then can update the game parameters

# Heist
# Scenes!

# Scene is the base class that the others come from
class Scene(object):
	def __init__(self):
		pass
# The action-menu in every scene is the same, although the results
#   are different. So the action-menu code is here,
#   but the code to handle the action is defined
#   in each scene's start function
	def action_menu(self):
		print "Go   Steal   Pick Lock   Use   Sap   Look   Wait   Menu"
		# in case of someone typing in all caps or matching
		#  the case shown in the menu, .lower() converts to lower
		#  case before returning
		return raw_input("> ").lower()

# the decision was made to store important game parameters 
#   in a dict game_objects
# start is the main() style entry point for a scene
	def start(self, game_objects):
		print "The start method for this scene is not yet implemented."
		print "received game_objects ", game_objects
		return "error"

# when we call the go menu, we have to reference many things
#   including the last room, and that requires passing up
#   our choice to the map 
	def go(self, game_objects):
		print "You may go:\nBACK   ",
		for i in game_objects['go']:
			print i.upper(), "   ",
		print "CANCEL"
		while True:
			inp = raw_input(">").lower()   #always lower the input case
			if inp == "back" or inp == "cancel":
				return inp
			else:
				for i in game_objects['go']:
					if inp == i:
						return inp
			# If we made it this far, the input wasn't recognized
			print "I'm sorry, I'm not sure what you meant."
			
