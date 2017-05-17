import random

WIDTH = 3
HEIGHT = 4

class agent():
	
 	def __init__(self):
		self.x_agent = 0
		self.y_agent = 0
		
	def agent_move_left(self):
		if x_agent - 1 >= 0:
			x_agent = x_agent - 1
		else:
			x_agent = x_agent
		return x_agent
	
	def agent_move_right(self):
		if x_agent + 1 <= 2:
			x_agent = x_agent + 1
		else:
			x_agent = x_agent
		return x_agent
	
	def agent_move_up(self):
		if y_agent - 1 >= 0:
			y_agent = y_agent - 1
		else:
			y_agent = y_agent
		return y_agent
		
	def agent_move_down(self):
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