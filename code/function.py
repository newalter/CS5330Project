
from math import log2

def function(n, k, d):
	roh = k / n

	num = 2 ** (-1 * roh * log2(roh) - (1 - roh) * log2(1 - roh))
	numerator = ((roh ** 2) * (n ** 2) * d - roh * n) 
	denominator = ((roh ** 2) * (n ** 2) * d - 2 * roh * n + n)

	fraction = (numerator / denominator) ** roh
	num = num * fraction
	return num


def function_roh(n, roh, d):
	num = 2 ** (-1 * roh * log2(roh) - (1 - roh) * log2(1 - roh))
	numerator = ((roh ** 2) * (n ** 2) * d - roh * n) 
	denominator = ((roh ** 2) * (n ** 2) * d - 2 * roh * n + n)

	fraction = (numerator / denominator) ** roh
	num = num * fraction
	return num


def function_roh_num(n, roh, d):
	num = 2 ** (-1 * roh * log2(roh) - (1 - roh) * log2(1 - roh))
	numerator = ((roh ** 2) * (n ** 2) * d - roh * n) 
	denominator = ((roh ** 2) * (n ** 2) * d - 2 * roh * n + n)

	fraction = (numerator / denominator) ** roh
	return num

for i in range(10):
	step = 0.13 + 0.001 * i
	print("AAAAAAAAAAAAAAAAAA", function_roh(10**10, step, 10))
	print("BBBBBBBBBBBBB", function_roh_num(10**10, step, 10))

# surd n
# log n
# 0.1 n
# 0.4 n
"""
0.1 = 1.38
0.2 = 1.649
0.3 = 1.842
0.4 = 1.96
0.5 = 2.00
"""

