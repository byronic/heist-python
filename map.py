class Map(object):
	def __init__(self):
		self.game_objects = {
			'power': True,
			'go': [],
			} # end self.game_objects
		self.current_scene = 'none'
		self.last_scene = 'none'

	def change_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

	def closing_scene(self):
		pass
