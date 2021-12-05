import sys
import datetime
import queue
import itertools
import copy
import time

from constraintProblem import CSP

#Plain DFSB
#backsearch = Backtracking-Search
#recurback = Recursive-Backtracking

steps = 0

def backsearch(csp):
	global steps
	steps = 0
	assignment = csp.initial_assignment()
	return recurback(assignment,csp)

def recurback(assignment,csp):
	global steps
	steps += 1
	#Check if assignment is complete
	if csp.complete(assignment):
		return assignment
	var = csp.select_unassigned_variable(assignment)
	for color in range(csp.colors):
		if csp.color_consistent(color,var,assignment):
			assignment[var] = color
			result = recurback(assignment,csp)
			#if path dead not lead to a dead end, return assignment, else backtrack by removing last assignment
			if result:
				return result
			assignment[var] = None
	return None

def backsearchplus(csp):
	global steps
	steps = 0
	#Setting up initial assignment for all variables with no colors, domain for all variables with all colors, and arc queue of all pairs of variables
	assignment = csp.initial_assignment()
	domain = csp.initial_domain()
	initial_arc_queue = csp.initial_arc_queue()
	return recurbackplus(domain,assignment,csp,initial_arc_queue)

def recurbackplus(domain,assignment,csp,initial_arc_queue):
	global steps
	steps += 1
	if csp.complete(assignment):
		return assignment
	ac3(csp,domain,initial_arc_queue)
	var = csp.most_constrained_variable(assignment,domain)
	least_constraining_values = csp.least_constraining_values(var,domain)
	for color in least_constraining_values:
		if csp.color_consistent(color,var,assignment):
			changes = csp.assign_color(var,color,domain,assignment)
			result = recurbackplus(domain,assignment,csp,initial_arc_queue)
			if result:
				return result
			assignment[var] = None
			for neighbor in changes:
				if color not in domain[neighbor]:
					domain[neighbor].append(color)
	return None

def ac3(csp,domain,initial_arc_queue):
	arc_queue = initial_arc_queue         
	while not arc_queue.empty():
		xi,xj = arc_queue.get()
		#check if we need to remove inconsistent values and if so, add the neighbors back into the queue
		if remove_inconsistent_values(csp,xi,xj,domain):
			for v1,v2 in csp.constraints:
				if v1 == xi:
					arc_queue.put((v2,xi))
				elif v2 == xi:
					arc_queue.put((v1,xi))

def remove_inconsistent_values(csp,xi,xj,domain):
	removed = False
	#check if xi and xj ar neighbors and if so, if there exists a variable y in domain of xj that is consistent for each variable x in domain of xi
	for v1,v2 in csp.constraints:
			if v1 == xi and v2 == xj:
				for x in domain[xi]:
					if len(domain[xj]) == 1 and x in domain[xj]:
						domain[xi].remove(x)
						removed = True
						return removed
			elif v1 == xj and v2 == xi:
				for x in domain[xi]:
					if len(domain[xj]) == 1 and x in domain[xj]:
						domain[xi].remove(x)
						removed = True
						return removed
	return removed

if __name__ == '__main__':
	if len(sys.argv) == 4:
		csp = CSP(sys.argv[1])
		print(csp)
		if int(sys.argv[3]) == 0:
			print("Plain:")
			start = datetime.datetime.now()
			assignment = backsearch(csp)
			stop = datetime.datetime.now()
			print(f"Time (in milliseconds): {(stop-start).total_seconds()*1e3}")
			csp.output_assignment(assignment,sys.argv[2])
			print(f"Steps: {steps}")
		else:
			print("Improved:") 
			start = datetime.datetime.now()
			assignment = backsearchplus(csp)
			stop = datetime.datetime.now()
			print(f"Time (in milliseconds): {(stop-start).total_seconds()*1e3}")
			csp.output_assignment(assignment,sys.argv[2])
			print(f"Steps: {steps}")
	else:
		csp = CSP("100_4_2500")
		print(csp)
		print("Result:")
		start = datetime.datetime.now()
		print(backsearchplus(csp))
		stop = datetime.datetime.now()
		print(f"Time (in milliseconds): {(stop-start).total_seconds()*1e3}")
		print(f"Steps: {steps}")
