number = int(input("Sayıyı Giriniz : "))

temp = number
reverse = 0
lastNum = 0

print(temp, reverse, lastNum)

while temp != 0 :
    lastNum = temp % 10
    reverse = (reverse * 10) + lastNum
    temp = int(temp / 10)

if reverse == number :
    print("Sayı Polindrom Bir Sayıdır.")
else :
    print("Sayı Polindrom Bir Sayı Değildir.")