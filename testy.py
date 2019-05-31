
find=input("what are you looking for : ")
replace=input("replace with what : ")
file_read=open("data.txt", "r")
file_write=open("data2.txt", "w")

for data in file_read:
	i=0
	while i<len(data):
		if data[i]==find[0]:
			if data[i:len(find)+i]==find:
				print(replace, end="",file=file_write)
				i+=len(find)-1
			else:
				print(data[i],end="",file=file_write)
		else:
			print(data[i],end="",file=file_write)
		i+=1