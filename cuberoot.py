# Verify that 2017 is the smallest number whose cube root begins with 10 distinct digits

from __future__ import division

def cube_root(input, precision=10):
	return str(input ** (1 / 3))[:precision + 1]

def contains_all_digits(input):
	for i in [str(n) for n in range(10)]:
		if i not in input:
			return False
	return True

for i in range(2018):
	result = cube_root(i)
	if contains_all_digits(result):
		print i, result