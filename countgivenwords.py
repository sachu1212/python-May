message=input("Enter any message:")
find=input("what are you looking for:")
i=0
f=0
while i<len(message):
	if message[i]==find[0]:
		if message[i:i+len(find)]==find:
			f=f+1
			i=i+len(find)-1
	i=i+1
print(f)
	