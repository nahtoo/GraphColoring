import re
import numpy as np
import itertools
import queue
import random

firstLine = re.compile(r"(\d+)\s(\d+)\s(\d+)")
constraintLines = re.compile(r"(\d+)\s(\d+)")

class CSP:

	def __init__(self,input_file):
		with open(input_file,'r') as fread:
			match = firstLine.match(fread.readline())
			self.variables = int(match.group(1))
			self.colors = int(match.group(3))
			self.constraints = []
			while True:
				input_line = fread.readline()
				if not input_line:
					break
				match = constraintLines.match(input_line)
				self.constraints.append((int(match.group(1)),int(match.group(2))))

	def goal_test(self,assignments):
		goal = True
		for v1,v2 in self.constraints:
			if assignments[v1] and assignments[v1] == assignments[v2]:
				goal = False
		return 

	def initial_assignment(self):
		return dict([(n,None) for n in range(self.variables)])

	def initial_domain(self):
		return dict([(n,([i for i in range(self.colors)])) for n in range(self.variables)])

	def initial_arc_queue(self):
		arc_queue = queue.Queue()
		[arc_queue.put(x) for x in (itertools.permutations([i for i in range(self.variables)], 2))]
		return arc_queue


	def complete(self,assignment):
		for var,color in assignment.items():
			if color is None:
				return False
		else: 
			return True

	def correct(self,assignment):
		for var,color in assignment.items():
			if not self.color_consistent(color,var,assignment):
				return False
		return True

	def select_unassigned_variable(self,assignment):
		for var,color in assignment.items():
			if color is None:
				return var	
		return None

	def color_consistent(self,color,var,assignment):
		for v1,v2 in self.constraints:
			if v1 == var:
				if assignment[v2] == color:
					return False
			elif v2 == var:
				if assignment[v1] == color:
					return False
		return True

	def select_random_variable(self,assignment):
		while True:
			random_var = random.randrange(self.variables)
			if not self.color_consistent(assignment[random_var],random_var,assignment):
				return random_var
		return None

	def most_constrained_variable(self,assignment,domain):
		constrained_variables = {}
		for var in range(self.variables):
			if assignment[var] is None:
				constrained_variables[var] = len(domain[var])
		sorted_constrained_variables = sorted(constrained_variables, key=constrained_variables.get)
		return sorted_constrained_variables[0]

	def least_constraining_values(self,var,domain):
		possible_values = {}
		for color in domain[var]:
			ruled_out = 0
			for v1,v2 in self.constraints:
				if v1 == var:
					if color in domain[v2]:
						ruled_out += 1
				elif v2 == var:
					if color in domain[v1]:
						ruled_out += 1
			possible_values[color] = ruled_out
		sorted_values = sorted(possible_values, key=possible_values.get)
		return sorted_values

	def min_conflict_value(self,var,assignment):
		possible_values = {}
		neighbors = []
		for v1,v2 in self.constraints:
			if v1 == var:
				neighbors.append(v2)
			elif v2 == var:
				neighbors.append(v1)
		for color in range(self.colors):
			conflict = 0
			for neighbor in neighbors:
				if assignment[neighbor] == color:
					conflict += 1
			possible_values[color] = conflict
		min_conflict_value = min(possible_values.values())
		min_values = [value for value in possible_values if possible_values[value] == min_conflict_value]
		return min_values[random.randrange(len(min_values))]

	def assign_color(self,var,color,domain,assignment):
		assignment[var] = color
		changes = []
		for v1,v2 in self.constraints:
			if v1 == var:
				if color in domain[v2]:
					domain[v2].remove(color)
					changes.append(v2)
			elif v2 == var:
				if color in domain[v1]:
					domain[v1].remove(color)
					changes.append(v1)
		return changes

	def output_assignment(self,assignment,output_file):
		with open(output_file,'w') as fwrite:
			for color in assignment.values():
				fwrite.write(str(color)+"\n")

	def __repr__(self):
		return str(f"{self.variables},{self.colors}")+'\n'+str(self.constraints)