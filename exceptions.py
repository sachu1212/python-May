try:
	No1=(int(input("Enter 1st Number : ")))
	No2=(int(input("Enter 2nd Number : ")))

	result=No1/No2
	print("Result is :", result)

except ValueError:
	print("Please use only digits")
except ZeroDivisionError:
	print("can't divide any numbers by 0")
