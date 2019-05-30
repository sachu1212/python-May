def reverse(word):
	newword=""
	i=len(word)-1
	while i>=0:
		newword=newword+word[i]
		i-=1
	return newword

message=input("Enter any message : ")
newmessage=""
word=""

for ch in message:
	if ch==" ":
		newmessage+=(reverse(word)+ " ")
		word=""
	else:
		word+= ch
newmessage += reverse(word)

print(newmessage)