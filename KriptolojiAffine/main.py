def sifreleme(sifrelenecekMesaj, A, B):
    harf = 0
    sifreli_mesaj = ""
    str(sifrelenecekMesaj).lower()
    for i in range(len(sifrelenecekMesaj)):
        harf = (alfabeList.get(sifrelenecekMesaj[i]) * A) + B
        harf = harf % 29
        sifreli_mesaj = sifreli_mesaj + str(list(alfabeList.keys())[list(alfabeList.values()).index(harf)])
    return sifreli_mesaj

def ondalıklıModül(sayi):
    denk = 0
    for i in range(500):
        if (sayi * i) % 29 == 1:
            denk = i
            break
    return denk

def sifreCözme(sifreli_mesaj, A, B):
    harf = 0
    cözülmüsMetin = ""
    str(sifreli_mesaj.lower())
    for i in range(len(sifreli_mesaj)):
        harf = (alfabeList.get(sifreli_mesaj[i]) - B)
        if harf < 0:
            harf += 29
        harf *= ondalıklıModül(A)
        harf %= 29
        cözülmüsMetin = cözülmüsMetin + str(list(alfabeList.keys())[list(alfabeList.values()).index(harf)])
    return cözülmüsMetin

degerA = 0
degerB = 0
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
alfabeList = dict()
for i in enumerate(alfabe, 1):
    alfabeList[i[1]] = i[0]

while True:
    sifrelenecek_mesaj = input("Lütfen Şifrelenmesini İstediğiniz Mesajı Giriniz")
    if str(sifrelenecek_mesaj).isalpha():
        print("Şimdi 2 değer gireceksiniz. Bu sayılar 1 den büyük eşit 29 dan küçük olmak zorundadır.\n 1 =< a,b < 29")
        break
    else:
        print("Geçersiz metin lütfen sadece harf girinizi...")

while True:
    degerA = input("A degerini giriniz")
    degerA = int(degerA)
    if 1 <= degerA < 29 and str(degerA).isdigit():
        print("Değer Kabul Edildi.")
        degerB = input("Şimdi b degerini giriniz")
        degerB = int(degerB)
        if degerA < degerB < 29 and str(degerB).isdigit():
            print("Değerler Kabul Edildi")
            break
        else:
            print("b değeri a değerinden büyük olmak zorunda")
    else:
        print("Girdiğiniz değer geçersiz bunun sebebi aralıklar veya harf girmeniz...")

print(sifreleme(sifrelenecek_mesaj, degerA, degerB))
sifrelenmis_mesaj = sifreleme(sifrelenecek_mesaj, degerA, degerB)
print(sifreCözme(sifrelenmis_mesaj,degerA,degerB))
