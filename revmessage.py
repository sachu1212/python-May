def change(message):
	i=0
	newmessage=""
	while i<len(message):
			if ord(message[i])>=65 and ord(message[i])<=90:
					newmessage+=chr(ord(message[i])+32)
			else:
				if ord(message[i])>=90 and ord(message[i])<=122:
					newmessage+=chr(ord(message[i])-32)
			
				else:
					if ord(message[i])>=48 and ord(message[i])<=57:
						newmessage+=str(int(message[i])*2)
					else:
						newmessage+=message[i]	
			i+=1
	print(newmessage)

change("ABC67%^*//")		
