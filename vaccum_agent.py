"""
	this practice aiming at build a environment and its vaccum cleaner agent
	the environment size can be pre-defined, and it is a mahattan map, each
	square has a chance to get dirty. the agent is designed to clean up the 
	dirty squares. 
"""


import random


WIDTH = 3
HEIGTH = 4


class environment:

	def __init__(self):
		self.x_map = 0
		self.y_map = 0
		self.matrix_map = [[0 for i in range(HEIGTH)] for j in range(WIDTH)]
		
	def dirt_generator(self):
		for i in range(WIDTH * HEIGTH):
			self.x_map = random.randint(0, WIDTH-1)
			self.y_map = random.randint(0, HEIGTH-1)
			print("{},{}".format(self.x_map, self.y_map))
			self.matrix_map[self.x_map][self.y_map] = 1
		return self.matrix_map

def main():
	environment_01 = environment()
	print(environment_01.matrix_map)
	
	environment_01.dirt_generator()
	print(environment_01.matrix_map)
	