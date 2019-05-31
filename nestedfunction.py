def opertions(day):
	if day==1:
		def fun(a,b):
			c=a+b
			print("The Result is :", c)
	if day==2:
		def fun(a,b):
			c=a-b
			print("The Result is :", c)
	return fun

ben=opertions(1)
ben(5,2)