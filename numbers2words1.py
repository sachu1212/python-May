ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
answer=""
num=int(input("Enter any number :"))
if num>=1000 and num<9999:
	answer+=ones[int(num/1000)]+ " thousand "
	num=num%1000
if num>=100:
	answer+=ones[int(num/100)]+" hundred "
	num=num%100
if num>=20:
	answer+=tens[int(num/10)] + " "
	num=num%10
if num>0 and num<=19:
	answer+=ones[num]
print(answer)