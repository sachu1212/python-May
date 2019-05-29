Alpha=input("Enter any character:")
if ord(Alpha)>=65 and ord(Alpha)<=90:
	print("UPPER CASE")
else:
	if ord(Alpha)>=97 and ord(Alpha)<=122:
		print("lower case")
	else:
		if ord(Alpha)>=48 and ord(Alpha)<=57:
			print("Digits")
		else:
			print("Special character")