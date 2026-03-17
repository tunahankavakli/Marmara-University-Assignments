def tarih_formatla(tarih):
    if "-" in tarih and "/" in tarih:
        print("Geçersiz tarih formatı!")
        return

    if "-" in tarih:
        ayir=tarih.split("-")
        ileri1="/".join(ayir)
        ileri2="-".join(ayir)

        ters=ayir[::-1]
        geri1="/".join(ters)
        geri2="-".join(ters)

        print(ileri1)
        print(ileri2)
        print(geri1)
        print(geri2)

    elif "/" in tarih:
        ayir=tarih.split("/")
        ileri1="-".join(ayir)
        ileri2="/".join(ayir)

        ters=ayir[::-1]
        geri1="-".join(ters)
        geri2="/".join(ters)

        print(ileri1)
        print(ileri2)
        print(geri1)
        print(geri2)

    else:
        print("Geçersiz tarih formatı!")

tarih=input("Tarih: ")
tarih_formatla(tarih)