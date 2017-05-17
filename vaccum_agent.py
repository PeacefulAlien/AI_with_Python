"""
	this practice aiming at build a environment and its vaccum cleaner agent
	the environment size can be pre-defined, and it is a mahattan map, each
	square has a chance to get dirty. the agent is designed to clean up the 
	dirty squares. 
"""


import random


WIDTH = 3
HEIGHT = 4

class environment:

	def __init__(self):
		self.x_map = 0
		self.y_map = 0
		self.matrix_map = [[0 for i in range(HEIGHT)] for j in range(WIDTH)]
		
	def dirt_generator(self):
		for i in range(WIDTH * HEIGHT):
			self.x_map = random.randint(0, WIDTH-1)
			self.y_map = random.randint(0, HEIGHT-1)
			print("{},{}".format(self.x_map, self.y_map))
			self.matrix_map[self.x_map][self.y_map] = 1
		return self.matrix_map

class agent():

	def __init__(self):
		self.x_agent = random.randint(0, WIDTH-1)
		self.y_agent = random.randint(0, HEIGHT-1)
	
	def move_left(self):
		if x_agent - 1 >= 0:
			x_agent = x_agent - 1
		else:
			x_agent = x_agent
		return x_agent
	
	def move_right(self):
		if x_agent + 1 <= 2:
			x_agent = x_agent + 1
		else:
			x_agent = x_agent
		return x_agent
	
	def move_up(self):
		if y_agent - 1 >= 0:
			y_agent = y_agent - 1
		else:
			y_agent = y_agent
		return y_agent
		
	def move_down(self):
		if y_agent + 1 <= 3:
			y_agent = y_agent + 1
		else:
			y_agent = y_agent
		return y_agent
	
	def agent_clean(self, status):
		if status == 1:
			print('''
				The current square is dirty.
				Vaccum agent is working on it...
				''')
			status = 0
		return status
	
	
def test_environment():
	environment_01 = environment()
	print(environment_01.matrix_map)
	
	environment_01.dirt_generator()
	print(environment_01.matrix_map)

def test_agent():
	agent_01 = agent()
	print("({},{})".format(agent_01.x_agent, agent_01.y_agent))
	
	agent_01.
	
	
	