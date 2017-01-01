# Find numbers that satisfy phi(n) = phi(n - 1) + phi(n - 2), where phi is the Euler totient function

from fractions import gcd

def phi(n):
	count = 0
	for i in range(1, n + 1):
		if gcd(n, i) == 1:
			count += 1
	return count

for i in range(2, 2018):
	if phi(i) == phi(i - 1) + phi(i - 2):
		print i, phi(i)

# Result:
# 2 1
# 3 2
# 5 4
# 7 6
# 11 10
# 17 16
# 23 22
# 37 36
# 41 40
# 47 46
# 101 100
# 137 136
# 233 232
# 257 256
# 857 856
# 1037 960
# 1297 1296
# 1541 1452
# 1601 1600
# 2017 2016