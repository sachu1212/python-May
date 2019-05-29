def Tax(salary):
	if salary>1500:
		T=salary*21/100
	else:
		T=salary*15/100
	return T



salary1=int(input("Enter your salary:"))
print("Your Tax is:", Tax(salary1))
print("Your Net Salary is:", (salary1-Tax(salary1)))