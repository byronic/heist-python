from rooms.entrancehall import EntranceHall
from rooms.billiardroom import BilliardRoom
from rooms.outside import Outside
from rooms.upstairslanding import UpstairsLanding
from rooms.ballroom import Ballroom
from rooms.kitchen import Kitchen
from rooms.study import Study
from rooms.bedrooms import Bedrooms
from rooms.library import Library
from rooms.electricalroom import ElectricalRoom

class Map(object):
	def __init__(self):
		self.game_objects = {
			'power': True,
			'go': [],
			'turn': 0,
			'heist complete': False
			} # end self.game_objects
		self.current_scene = 'entrance hall'
		self.last_scene = 'none'
		self.scenes = {
			'entrance hall': EntranceHall(),
			'outside': Outside(),
			'billiard room': BilliardRoom(),
			'upstairs landing': UpstairsLanding(),
			'ballroom': Ballroom(),
			'study': Study(),
			'kitchen': Kitchen(),
			'bedrooms': Bedrooms(),
			'library': Library(),
			'electrical room': ElectricalRoom()
			}
		# these are the links for all the rooms --
		#    meaning a hashtable of arrays containing the possible 
		#    destinations to 'go' when in the hash'd room
		self.links = {
			'entrance hall': [ 'outside', 'billiard room', 'upstairs landing', 'ballroom' ],
			'outside': [ 'entrance hall' ],
			'billiard room': [ 'study', 'kitchen', 'entrance hall' ],
			'upstairs landing': [ 'entrance hall', 'library', 'bedrooms' ],
			'ballroom': [ 'entrance hall' ],
			'study': [ 'billiard room' ],
			'kitchen': [ 'billiard room' ],
			'bedrooms': [ 'upstairs landing' ],
			'library': [ 'electrical room', 'upstairs landing' ],
			'electrical room': [ 'library' ]
			} # end self.links
		self.game_over = """
You were arrested!
Game over.
"""
		self.game_win = """
With a sigh of relief, you drive away.
The statuette is safely tucked in your coat,
a comforting lump despite it occasionally 
digging into your ribs.

You have completed the heist!
"""
	# end def __init__(self)

# TODO: Add the actual code for this (and call from opening_scene()) or remove entirely
	def change_scene(self, scene_name):
		pass

# TODO: Should this just be 'start' and we lose closing scene?
#       If so, we can only return the result to engine when we're sure all is finished
#       or if we need the pause menu
	def opening_scene(self):
		while True:
			self.set_links()
			# TODO: missing handling for sap, use, pick lock, and steal
			result = self.scenes[self.current_scene].start(self.game_objects)
			if result == "wait":
				self.game_objects['turn'] += 1
			elif result == "pause":
				return "pause"
			elif result == "error":
				return "error"
			elif result == "game_over":
				print self.game_over
				print "\nPress <RETURN> after you swallow your shame.",
				raw_input()
				return "done"
			elif result == "game_win":
				print self.game_win
				print "\nPress <RETURN> when you are done basking.\n\n"
				raw_input()
			else: # we were told to go somewhere
			      # TODO: you could conceivably put this into change_scene
				self.game_objects['turn'] += 1
				if result == "back":
					if self.last_scene != "none":
						temp = self.last_scene
						self.last_scene = self.current_scene
						self.current_scene = temp
				else:
					self.last_scene = self.current_scene
					self.current_scene = result

# This initializes the game_objects['go'] array based on the self.current_scene
	def set_links(self):
		self.game_objects['go'] = self.links[self.current_scene]

# TODO: necessary?
	def closing_scene(self):
		pass
