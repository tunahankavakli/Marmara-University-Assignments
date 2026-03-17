cumle=input("Bir cümle giriniz: ")

kelimeler=[]
kelime=""
for i in range(len(cumle)):
    if cumle[i]!=" ":
        kelime=kelime+cumle[i]
    else:
        if kelime!="":
            kelimeler.append(kelime)
            kelime=""

if kelime!="":
    kelimeler.append(kelime)

en_uzun_kelime=kelimeler[0]
for i in range(1,len(kelimeler)):
    if len(kelimeler[i])>len(en_uzun_kelime):
        en_uzun_kelime=kelimeler[i]

print("En uzun kelime:",en_uzun_kelime)
