def uppercase(str):
	x = 0
	while str[x] != 0:
		if ord(str[x]) >= 97 and ord(str[x]) <= 122:
			print(chr(ord(str[x]) - 32), end="")
		else:
			print(chr(ord(str[x])), end="")
		x += 1
