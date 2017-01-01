# Verify that 2017 is the smallest natural number able to be expressed as a multi-digit palindrome in two consecutive bases

def is_palindrome(input):
	pass

def convert_to_base(input, base):
	pass

for i in range(2018):
	for base in range(2, i - 1):
		result1 = convert_to_base(i, base)
		result2 = convert_to_base(i, base + 1)
		if is_palindrome(result1) and is_palindrome(result2):
			print base, result1, base + 1, result2