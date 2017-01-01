# Check if 2017 is the smallest natural number able to be expressed as a multi-digit palindrome in two consecutive bases

def is_palindrome(input):
	for i in range(len(input) / 2):
		if not (input[i] == input[len(input) - i - 1]):
			return False
	return True

def convert_to_base(input, base):
	result = []
	while input > 0:
		result.append(input % base)
		input /= base
	return result

for i in range(2018):
	for base in range(2, i - 1):
		result1 = convert_to_base(i, base)
		result2 = convert_to_base(i, base + 1)
		if is_palindrome(result1) and is_palindrome(result2):
			print i, base, result1, base + 1, result2

# Output:
# 10 3 [1, 0, 1] 4 [2, 2]
# 46 4 [2, 3, 2] 5 [1, 4, 1]
# 67 5 [2, 3, 2] 6 [1, 5, 1]
# 92 6 [2, 3, 2] 7 [1, 6, 1]
# 98 5 [3, 4, 3] 6 [2, 4, 2]
# 104 5 [4, 0, 4] 6 [2, 5, 2]
# 121 7 [2, 3, 2] 8 [1, 7, 1]
# 130 3 [1, 1, 2, 1, 1] 4 [2, 0, 0, 2]
# 135 6 [3, 4, 3] 7 [2, 5, 2]
# 154 8 [2, 3, 2] 9 [1, 8, 1]
# 178 6 [4, 5, 4] 7 [3, 4, 3]
# 178 7 [3, 4, 3] 8 [2, 6, 2]
# 185 6 [5, 0, 5] 7 [3, 5, 3]
# 191 9 [2, 3, 2] 10 [1, 9, 1]
# 227 8 [3, 4, 3] 9 [2, 7, 2]
# 232 10 [2, 3, 2] 11 [1, 10, 1]
# 235 7 [4, 5, 4] 8 [3, 5, 3]
# 277 11 [2, 3, 2] 12 [1, 11, 1]
# 282 9 [3, 4, 3] 10 [2, 8, 2]
# 292 7 [5, 6, 5] 8 [4, 4, 4]
# 300 7 [6, 0, 6] 8 [4, 5, 4]
# 300 8 [4, 5, 4] 9 [3, 6, 3]
# 326 12 [2, 3, 2] 13 [1, 12, 1]
# 343 10 [3, 4, 3] 11 [2, 9, 2]
# 373 8 [5, 6, 5] 9 [4, 5, 4]
# 373 9 [4, 5, 4] 10 [3, 7, 3]
# 379 13 [2, 3, 2] 14 [1, 13, 1]
# 410 11 [3, 4, 3] 12 [2, 10, 2]
# 436 14 [2, 3, 2] 15 [1, 14, 1]
# 446 8 [6, 7, 6] 9 [5, 4, 5]
# 454 10 [4, 5, 4] 11 [3, 8, 3]
# 455 8 [7, 0, 7] 9 [5, 5, 5]
# 464 9 [5, 6, 5] 10 [4, 6, 4]
# 483 12 [3, 4, 3] 13 [2, 11, 2]
# 497 15 [2, 3, 2] 16 [1, 15, 1]
# 543 11 [4, 5, 4] 12 [3, 9, 3]
# 555 9 [6, 7, 6] 10 [5, 5, 5]
# 562 13 [3, 4, 3] 14 [2, 12, 2]
# 562 16 [2, 3, 2] 17 [1, 16, 1]
# 565 10 [5, 6, 5] 11 [4, 7, 4]
# 631 17 [2, 3, 2] 18 [1, 17, 1]
# 640 12 [4, 5, 4] 13 [3, 10, 3]
# 646 9 [7, 8, 7] 10 [6, 4, 6]
# 647 14 [3, 4, 3] 15 [2, 13, 2]
# 651 5 [1, 0, 1, 0, 1] 6 [3, 0, 0, 3]
# 656 9 [8, 0, 8] 10 [6, 5, 6]
# 676 10 [6, 7, 6] 11 [5, 6, 5]
# 676 11 [5, 6, 5] 12 [4, 8, 4]
# 704 18 [2, 3, 2] 19 [1, 18, 1]
# 738 15 [3, 4, 3] 16 [2, 14, 2]
# 745 13 [4, 5, 4] 14 [3, 11, 3]
# 781 19 [2, 3, 2] 20 [1, 19, 1]
# 787 10 [7, 8, 7] 11 [6, 5, 6]
# 797 12 [5, 6, 5] 13 [4, 9, 4]
# 809 11 [6, 7, 6] 12 [5, 7, 5]
# 835 16 [3, 4, 3] 17 [2, 15, 2]
# 858 14 [4, 5, 4] 15 [3, 12, 3]
# 862 20 [2, 3, 2] 21 [1, 20, 1]
# 898 10 [8, 9, 8] 11 [7, 4, 7]
# 909 10 [9, 0, 9] 11 [7, 5, 7]
# 928 13 [5, 6, 5] 14 [4, 10, 4]
# 938 17 [3, 4, 3] 18 [2, 16, 2]
# 942 11 [7, 8, 7] 12 [6, 6, 6]
# 947 21 [2, 3, 2] 22 [1, 21, 1]
# 954 12 [6, 7, 6] 13 [5, 8, 5]
# 979 15 [4, 5, 4] 16 [3, 13, 3]
# 1036 22 [2, 3, 2] 23 [1, 22, 1]
# 1047 18 [3, 4, 3] 19 [2, 17, 2]
# 1069 14 [5, 6, 5] 15 [4, 11, 4]
# 1075 11 [8, 9, 8] 12 [7, 5, 7]
# 1108 16 [4, 5, 4] 17 [3, 14, 3]
# 1111 12 [7, 8, 7] 13 [6, 7, 6]
# 1111 13 [6, 7, 6] 14 [5, 9, 5]
# 1129 23 [2, 3, 2] 24 [1, 23, 1]
# 1162 19 [3, 4, 3] 20 [2, 18, 2]
# 1208 11 [9, 10, 9] 12 [8, 4, 8]
# 1220 11 [10, 0, 10] 12 [8, 5, 8]
# 1220 15 [5, 6, 5] 16 [4, 12, 4]
# 1226 24 [2, 3, 2] 25 [1, 24, 1]
# 1245 17 [4, 5, 4] 18 [3, 15, 3]
# 1268 12 [8, 9, 8] 13 [7, 6, 7]
# 1280 14 [6, 7, 6] 15 [5, 10, 5]
# 1283 20 [3, 4, 3] 21 [2, 19, 2]
# 1294 13 [7, 8, 7] 14 [6, 8, 6]
# 1327 25 [2, 3, 2] 26 [1, 25, 1]
# 1381 16 [5, 6, 5] 17 [4, 13, 4]
# 1390 18 [4, 5, 4] 19 [3, 16, 3]
# 1410 21 [3, 4, 3] 22 [2, 20, 2]
# 1425 12 [9, 10, 9] 13 [8, 5, 8]
# 1432 26 [2, 3, 2] 27 [1, 26, 1]
# 1461 15 [6, 7, 6] 16 [5, 11, 5]
# 1477 13 [8, 9, 8] 14 [7, 7, 7]
# 1491 14 [7, 8, 7] 15 [6, 9, 6]
# 1541 27 [2, 3, 2] 28 [1, 27, 1]
# 1543 19 [4, 5, 4] 20 [3, 17, 3]
# 1543 22 [3, 4, 3] 23 [2, 21, 2]
# 1552 17 [5, 6, 5] 18 [4, 14, 4]
# 1582 12 [10, 11, 10] 13 [9, 4, 9]
# 1595 12 [11, 0, 11] 13 [9, 5, 9]
# 1654 16 [6, 7, 6] 17 [5, 12, 5]
# 1654 28 [2, 3, 2] 29 [1, 28, 1]
# 1660 13 [9, 10, 9] 14 [8, 6, 8]
# 1682 23 [3, 4, 3] 24 [2, 22, 2]
# 1702 14 [8, 9, 8] 15 [7, 8, 7]
# 1702 15 [7, 8, 7] 16 [6, 10, 6]
# 1704 20 [4, 5, 4] 21 [3, 18, 3]
# 1733 18 [5, 6, 5] 19 [4, 15, 4]
# 1771 29 [2, 3, 2] 30 [1, 29, 1]
# 1827 24 [3, 4, 3] 25 [2, 23, 2]
# 1843 13 [10, 11, 10] 14 [9, 5, 9]
# 1859 17 [6, 7, 6] 18 [5, 13, 5]
# 1873 21 [4, 5, 4] 22 [3, 19, 3]
# 1892 30 [2, 3, 2] 31 [1, 30, 1]
# 1913 14 [9, 10, 9] 15 [8, 7, 8]
# 1924 19 [5, 6, 5] 20 [4, 16, 4]
# 1927 16 [7, 8, 7] 17 [6, 11, 6]
# 1943 15 [8, 9, 8] 16 [7, 9, 7]
# 1978 25 [3, 4, 3] 26 [2, 24, 2]
# 2017 31 [2, 3, 2] 32 [1, 31, 1]