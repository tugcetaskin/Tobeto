height = int(input("Boyunuzu Giriniz(cm) : "))
weight = int(input("Kilonuzu Giriniz : "))

height /= 100

index = weight / ( height *  height)

resultText = f"Vücut Kitle İndex'iniz : {index}"
print(resultText)