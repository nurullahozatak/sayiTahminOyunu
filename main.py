import random

number = random.randint(1, 100)
point = 100
correction = True

print("*************** Sayı Tahmin Oyunu *************** \n")
print("Toplam 100 puanınız var ve sayıyı tahmin etmek için 25 hakkınız bulunmakta\n")
while correction:
    guess = int(input("Sayı tahmin edin : "))
    if number < guess:
        print("Aşağı")
        point -= 5
    elif number > guess:
        print("Yukarı")
        point -= 5
    else:
        print("Kazandınız Doğru Tahmin!")
        print("Puanınız :" ,point)
        correction = False


