cev = "nar"

sor = "Carsidan aldim bir tane eve geldim Bintane nedir? :"

while True:
    veri = str(input(sor)).strip().lower()

    if veri != cev:
        print(veri, "Yanlis cevap!!!")
    else:
        print(">>>",veri,"<<<", " Tebrikler Bildin!")
        break