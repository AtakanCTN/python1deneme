liste = []                                      # 2 ILE 100 SAYI ARALIGINDAKI ASAL SAYILARI YAZAR.

for num in range(2,101):
    x = True
    for i in range(2,num):
        if num % i == 0:
            x = False
    if x :
        liste.append(num)
print(liste)
