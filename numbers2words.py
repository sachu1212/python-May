def ones(num):
	result=""
	if num==1:
		result="one"
	if num==2:
		result="two"
	if num==3:
		result="three"
	if num==4:
		result="four"
	if num==5:
		result="five"
	if num==6:
		result="six"
	if num==7:
		result="seven"
	if num==8:
		result="eight"
	if num==9:
		result="nine"
	if num==10:
		result="ten"
	if num==11:
		result="eleven"
	if num==12:
		result="twelve"
	if num==13:
		result="thirteen"
	if num==14:
		result="fourteen"
	if num==15:
		result="fifteen"
	if num==16:
		result="sixteen"
	if num==17:
		result="seventeen"
	if num==18:
		result="eighteen"
	if num==19:
		result="ninteen"
	return result

def tens(num):
	result=""
	if num==20:
		result=" twenty "
	if num==30:
		result=" thirty "
	if num==40:
		result=" fourty "
	if num==50:
		result=" fifty "
	if num==60:
		result=" sixty "
	if num==70:
		result=" seventy "
	if num==80:
		result=" eighty "
	if num==90:
		result=" ninty "
	return result	

num=int(input("Enter Any 4 digit number:"))
answer=""
if num>=1000 and num<=9999:
	answer+=ones(int(num/1000))+" thousand "
	num=num%1000

if num>=100:
	answer+=ones(int(num/100))+" hundred"
	num=num%100

if num>=20:
	answer+=tens((int(num/10))*10)
	num=num%10

if num>0 and num<=19:
	answer+=ones(num)

print(answer)