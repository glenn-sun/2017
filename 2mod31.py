# Verify that 2017 is the smallest prime congruent to 2 mod 31 that can be written a^2 + 24b^2 for some integers a, b

from math import floor

def is_prime(input):
	if input == 0 or input == 1:
		return False
	for i in range(2, int(floor(input ** 0.5)) + 1):
		if not input % i:
			return False
	return True

condition1 = set([31 * x + 2 for x in range(66)])
condition2 = set([a ** 2 + 24 * b ** 2 for a in range(45) for b in range(10) if a ** 2 + 24 * b ** 2 < 2018])

print [item for item in condition1 & condition2 if is_prime(item)]

# Output
# [2017]