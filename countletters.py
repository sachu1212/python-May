Message=input("Enter any Message:")
letter=input("What are you looking for:")
i=0
found=0
while i<len(Message):
	if Message[i]==letter:
		found=found+1
	i=i+1
print(found)