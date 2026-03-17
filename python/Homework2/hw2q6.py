yazi = input("Bir yazı giriniz: ")
sesli_harfler = "aeıioöuü"

yazi = yazi.lower()
Dict = {}

for harf in yazi:
    for i in range(len(sesli_harfler)):
        if harf == sesli_harfler[i]:
            if sesli_harfler[i] in Dict:
                Dict[sesli_harfler[i]] += 1
            else:
                Dict[sesli_harfler[i]] = 1

print(Dict)
