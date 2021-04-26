#!/usr/bin/python3
x = 97
while x < 123:
	if x == 101:
		x += 1
	elif x == 113:
		x += 1
	else:
		print(chr(x), end="")
		x += 1
