

# febnacii

# 0 1 1 2 3

a = 0
b = 1

res = 0

while res <  100:
	res = a + b
	print(res, end=" ")
	a = b
	b = res

while a < 100:
	print(a)
	a, b = b, a+b
