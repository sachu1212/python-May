def wordcount(message):
	word=1
	i=0
	while i<len(message):
		if message[i]==" ":
			word+=1
		i+=1
	return word

print("words:", wordcount("Hello my friends"))
print("words:", wordcount("I am back"))