import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sayi  = int(input("kaç harfli şifere istersin: "))
parola = ""


for i in range(sayi):
    parola += random.choice(karakter)


print("oluşturulan şifre",parola) 
