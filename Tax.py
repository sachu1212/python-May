name=input("Enter your Name:")
salary=int(input("Enter your Salary:"))
if salary>2000:
	tax=salary*25/100
else:
	tax=salary*15/100
netsalary=salary-tax
print("Your Name:",name)
print("Your Salary:", salary)
print("Your Tax:",tax)
print("Your Netsalary:", netsalary)