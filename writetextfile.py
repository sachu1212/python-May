F1=open("data.txt","r")
for data in F1:
	print(data)

file_read=open("data.txt","r")
file_write=open("data2.txt","w")
for data in file_read:
	print(data,file=file_write)