# Verify that 2017 is the smallest number whose cube root begins with 10 distinct digits

from __future__ import division

def cube_root(input, precision=10):
	pass

def contains_all_digits(input):
	pass

for i in range(2018):
	result = cube_root(i)
	if contains_all_digits(result):
		print i, result