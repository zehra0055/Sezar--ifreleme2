alfabe = ['a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z']

metin = input("Bir kelime giriniz: ").lower()
anahtar = int(input("Kaydırma miktarı: "))

sonuc = ""

for harf in metin:
    if harf in alfabe:
        index = alfabe.index(harf)
        yeni_index = (index + anahtar) % 26
        sonuc += alfabe[yeni_index]
    else:
        sonuc += harf

print("Şifreli metin:", sonuc)
