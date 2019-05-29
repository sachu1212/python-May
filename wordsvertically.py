message=input("Enter any message:")
word=""
i=0
while i<len(message):
	if message[i]==" ":
		print(word)
		word=""
	else:
		word=word+message[i]
	i=i+1
print (word)