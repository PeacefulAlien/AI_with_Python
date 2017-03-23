"""

"""


import random


WIDTH = 3
HEIGTH = 4


class environment:

	def __init__(self):
		self.x_map = 0
		self.y_map = 0
		self.matrix_map = [[0 for i in range(WIDTH)] for j in range(HEIGTH)]
		
	def dirt_generator(self):
		for i in range(WIDTH * HEIGTH):
			self.x_map = random.randint(0, WIDTH-1)
			self.y_map = random.randint(0, HEIGTH-1)
			self.matrix_map[self.x_map][self.y_map] = 1
		return self.matrix_map

if __name__ == '__main__':
	environment_01 = environment()
	print(environment_01.matrix_map)
	
	environment_01.dirt_generator()
	print(environment_01.matrix_map)
	