# Heist 1.0
# game engine!

# we must include the map b/c Engine holds the instance of it
from map import Map

class Engine(object):
	# __init__ only instantiates class-specific variables
	def __init__(self):
		self.map = Map()
		self.state = "main_menu"

	# This is the "main()-style" entry point for the Engine
	#   It must keep track of if we are in a menu, the game, or quitting
	#   It intentionally cannot see 'into' the game, but instead delegates that job
	#    to Map, passing control back and forth between in-class menus and the game.
	def start(self):
		print "Engine started."
		while True:
			if self.state == "main_menu":
				self.state = self.main_menu()
			elif self.state == "new_game":
				pass
			elif self.state == "load_game":
				pass
			elif self.state == "exit":
				break
		print "\n\n\nThanks for playing!"

	# This is the main menu for the game. It holds the user
	#  here until a true game-state is decided on by the player
	def main_menu(self):
		while True:
			print "Heist\n\nA game by eth0\n"
			print "1. Begin New Game"
			print "2. Load Game"
			print "3. Exit"
			inp = raw_input("> ")
			if inp == "1":
				return "new_game"
			elif inp == "2":
				return "load_game"
			elif inp == "3":
				return "exit"
			else:
				print "Sorry, I didn't understand. Choose either 1, 2, or 3."

	def load_game(self):
		pass

	def new_game(self):
		pass

	def in_game_menu(self):
		while True:
			print "Heist - Paused"
			print "1. Save Game"
			print "2. Quit and Return to Menu"
			inp = raw_input("> ")
			if inp == "1":
				return "save_game"
			elif inp == "2":
				return "quit_game"
			else:
				print "Sorry, I didn't understand. Choose either 1, 2, or 3."
