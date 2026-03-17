yazi=["Ahmet","altı","yaşında","Zeynep","dört","yaşında","Esra","iki","yaşında","Ayşe","bir","yaşında"]

sayilar={"bir":1,"iki":2,"üç":3,"dört":4,"beş":5,"altı":6,"yedi":7,"sekiz":8,"dokuz":9}

i=0
for kelime in yazi:
    if sayilar.get(kelime):
        yazi.remove(kelime)
        yazi.insert(i,sayilar.get(kelime))
    i+=1

print(yazi)