import random

kücük = "abcdefghklmnoprs"
büyük = "ABCDEFGHKLMNOPRS"
numaralar = "0123456789"
semboller = "[]{}()*;/.,_-"

ekle = kücük + büyük + numaralar + semboller

uzunluk = 18
sifre = "".join(random.sample(ekle, uzunluk))
f = open("sifrem.txt", "w")
f.write(sifre)