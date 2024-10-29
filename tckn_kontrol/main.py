girilen = input("Kimlik numaranızı giriniz:")
print(girilen)

if girilen.isnumeric():
    print(girilen, "sayısal değerdir.")
    if len(str(int(girilen))) == 11:
        print(girilen, "11 hanedir.")

if girilen.isnumeric() and len(str(int(girilen))) == 11:
    tckn = int(girilen)
    ilk9 = tckn // 100
    son2 = tckn % 100
    tekler, ciftler = 0, 0

    b = ilk9 % 10
    tekler += b
    ilk9 //=10

    b = ilk9 % 10
    ciftler += b
    ilk9 //= 10

    b = ilk9 % 10
    tekler += b
    ilk9 //= 10

    b = ilk9 % 10
    ciftler += b
    ilk9 //= 10

    b = ilk9 % 10
    tekler += b
    ilk9 //= 10

    b = ilk9 % 10
    ciftler += b
    ilk9 //= 10

    b = ilk9 % 10
    tekler += b
    ilk9 //= 10

    b = ilk9 % 10
    ciftler += b
    ilk9 //= 10

    b = ilk9 % 10
    tekler += b
    ilk9 //= 10


    b10 = (tekler * 7 - ciftler) % 10
    b11 = (tekler + ciftler + b10) %10

    if b10 * 10 + b11 == son2:
        print("Kimlik numarası tutarlıdır.")
    else:
        print("Kimlik numarası tutarsızdır.")

else:
    print(girilen, "Kimlik formatına uymamakta.")



