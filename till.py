Balance=int(input("Enter Balance:"))
notes50=Balance//50
Balance=Balance%50
notes20=Balance//20
Balance=Balance%20
notes10=Balance//10
Balance=Balance%10
notes5=Balance//5
Balance=Balance%5
coins2=Balance//2
Balance=Balance%2
coins1=Balance


if notes50>0:
	print("50=",notes50)
if notes20>0:
	print("20=",notes20)
if notes10>0:
	print("10=",notes10)
if notes5>0:
	print("5=",notes5)
if coins2>0:
	print("2=",coins2)
if coins1>0:
	print("1=",coins1)