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
			'heist complete': False,
			'guards': 0    # the number of guards in the room we're entering
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
		# for the guards,
		#  each room has a number of guards based on the turn
		self.guard_paths = {
			'library': [2, 1, 0, 0],
			'upstairs landing': [1, 2, 1, 2],
			'bedrooms': [0, 0, 2, 1],
			'study': [0, 0, 0, 1],
			'billiard room': [1, 0, 1, 0],
			'kitchen': [0, 1, 0, 0]
			} # end self.guard_paths
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
				# anytime the turn number goes up, we must move the guards
				self.move_guards()
				# TODO: ^^ to clean up turn/guard movement, 
				#    maybe make a turn increment function that calls everything?
			# adding sap logic here
			elif result == "sap":
				# successful saps always take out the lone guard
				for i in range(0, len(self.guard_paths[self.current_scene])):
					if self.guard_paths[self.current_scene][i] == 1:
						self.guard_paths[self.current_scene][i] = 0
				self.game_objects['turn'] += 1
				self.move_guards()
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
				# move the guards after we change rooms!
				self.move_guards()

# This initializes the game_objects['go'] array based on the self.current_scene
	def set_links(self):
		self.game_objects['go'] = self.links[self.current_scene]

# This calculates the number guards based on the current room
#    then puts that value into self.game_objects['guards']
	def move_guards(self):
		# this scary bit of code is actually necessary due to math;
		# although we could presume that len(self.guard_paths[self.current_scene]) is always
		# equal to four, it's better to calculate it
		try:
			self.game_objects['guards'] = self.guard_paths[self.current_scene][self.game_objects['turn'] % len(self.guard_paths[self.current_scene])]
		# The exception is necessary when the current scene does not exist; no action necessary
		except:
			pass

# TODO: necessary?
	def closing_scene(self):
		pass
