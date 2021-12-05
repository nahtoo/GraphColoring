import sys
import datetime
import queue
import itertools
import copy
import time
import random

from constraintProblem import CSP

steps = 0

# Min-conflicts algorithim
def min_conflicts(csp,assignment,max_steps):
	global steps
	for i in range(max_steps):
		steps += 1
		if csp.correct(assignment):
			return assignment	
		var = csp.select_random_variable(assignment)
		color = csp.min_conflict_value(var,assignment)
		assignment[var] = color
	return None

#entry point for Min-conflicts, used to call Min-conflicts initially and iteratively call again if it could not find a solution in max_steps
def min_conflicts_entry(csp):
	while True:
		assignment = csp.initial_assignment()
		for var in range(csp.variables):
			assignment[var] = random.randrange(csp.colors)
		final_assignment = min_conflicts(csp,assignment,10000)
		if final_assignment is not None:
			break
	return final_assignment

if __name__ == '__main__':
	if len(sys.argv) == 3:
		csp = CSP(sys.argv[1])
		print(csp)
		print("Min-conflict:")
		start = datetime.datetime.now()
		assignment = min_conflicts_entry(csp)
		stop = datetime.datetime.now()
		print(f"Time (in milliseconds): {(stop-start).total_seconds()*1e3}")
		csp.output_assignment(assignment,sys.argv[2])
		print(f"Steps: {steps}")
	else:
		csp = CSP("400_4_40000")
		print(csp)
		print("Result:")
		start = datetime.datetime.now()
		print(min_conflicts_entry(csp))
		stop = datetime.datetime.now()
		print(f"Time (in milliseconds): {(stop-start).total_seconds()*1e3}")