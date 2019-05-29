Alpha=input("Enter any Alphabet:")
if ord(Alpha)>=65 and ord(Alpha)<=90:
	print(chr(ord(Alpha)+32))
else:
	if ord(Alpha)>=97 and ord(Alpha)<=122:
		print(chr(ord(Alpha)-32))
