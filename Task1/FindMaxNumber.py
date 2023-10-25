num1 = int(input("1. Sayıyı Giriniz : "))
num2 = int(input("2. Sayıyı Giriniz : "))
num3 = int(input("3. Sayıyı Giriniz : "))

maxNum = num1

if num2 > maxNum :
    maxNum = num2
    if num3 > maxNum :
        maxNum = num3
else :
    if num3 > maxNum :
        maxNum = num3

print(maxNum)