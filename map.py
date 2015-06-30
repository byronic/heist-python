from entrancehall import EntranceHall
from billiardroom import BilliardRoom
from outside import Outside
from upstairs import Upstairs
from ballroom import Ballroom

class Map(object):
	def __init__(self):
		self.game_objects = {
			'power': True,
			'go': [],
			'turn': 0
			} # end self.game_objects
		self.current_scene = 'entrance hall'
		self.last_scene = 'none'
		self.scenes = {
			'entrance hall': EntranceHall(),
			'outside': Outside(),
			'billiard room': BilliardRoom(),
			'upstairs': Upstairs(),
			'ballroom': Ballroom()
			}

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
				turn += 1
			elif result == "pause":
				return "pause"
			elif result == "error":
				return "error"
			else: # we were told to go somewhere
			      # TODO: you could conceivably put this into change_scene
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
		if self.current_scene == "entrance hall":
			self.game_objects['go'] = [ 'outside', 'billiard room', 'upstairs', 'ballroom']
		# TODO: a whole lot more of this to write

# TODO: necessary?
	def closing_scene(self):
		pass
