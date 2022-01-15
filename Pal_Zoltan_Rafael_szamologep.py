print("Kerem valasszi ki melyik szamolasi modot szeretne alkalmazni az alabbiak kozul!")
print("1. Osszeadas")
print("2. Kivonas")
print("3. Szorzas")
print("4. Osztas")
print("5. Pitagorasz tetel")
print("6. Kor kerulete ")
print("7. Kor terulete ")
print("8. Teglalap kerulete ")
print("9. Teglalap terulete ")
print("10. Haromszog kerulete ")
print("11. Haromszog terulete ")
print("12. Negyzet kerulete")
print("13. Negyzet terulete")
szamok = input("Ide irja be a kivant megoldokeplet NEVET a fentiek kozul!: ")

if szamok == "Osszeadas":
    print("Az osszeadas megoldokeplete: A + B")
    szam1 = int(input("Kerek egy szamot!: "))
    szam2 = int(input("Kerek megegy szamot!: "))
    megoldas = szam1 + szam2
    print("A megoldas!: ", megoldas)

elif szamok == "Kivonas":
    print("A kivonas megoldokeplete: A - B")
    szam1 = int(input("Adjon meg egy szamot!: "))
    szam2 = int(input("Adjon meg megegy szamot!: "))
    megoldas = (szam1 - szam2)
    print("A vegeredmeny!:", megoldas)

elif szamok == "Szorzas":
    print("A szorzas megoldokeplete: A * B")
    szam1 = int(input("Adjon meg egy szamot!: "))
    szam2 = int(input("Adjon meg egy masik szamot!: "))
    megoldas = szam1 * szam2
    print("A vegeredmeny!: ", megoldas)

elif szamok == "Osztas":
    print("Az osztas megoldokeplete: A / B")
    szam1 = int(input("Irjon be szamot!: "))
    szam2 = int(input("Adjon meg megegy szamot!: "))
    megoldas = szam1 / szam2
    print("A vegeredmeny", megoldas, "lett")

elif szamok == "Pitagorasz tetel":
    print("A Pitagorasz tetel megoldokeplete: A*A + B*B = C*C") 
    szam1 = int(input("Ide irja a szamot:! "))
    szam2 = int(input("Irjon be megegy szamot kerem!: "))
    megoldas = szam1 * szam1 + szam2 * szam2
    print("A vegeredmenye", megoldas, "lett!")

elif szamok == "Kor kerulete":
    print("A Kor keruletenek a megoldokeplete: 2 * r * Pi")
    radiusz = int(input("Kerem adja meg az r erteket!: "))
    megoldas = 2 * radiusz * 3.14
    print("A kor keruletenek az erteke", megoldas, "kobmeter lett!")

elif szamok == "Kor terulete":
    print("A Kor teruletenek a megoldokeplete: r * r * Pi ")
    radiusz = int(input("Kerem adja meg az r erteket!: "))
    megoldas = radiusz * radiusz * 3.14
    print("A kor teruletenek az erteke", megoldas, "negyzetmeter lett!")

elif szamok == "Teglalap kerulete":
    print("A Teglalap keruletenek a megoldokeplete: (A * B) * 2")
    print("Kerem adja meg az ertekeket meterben")
    szam1 = int(input("Irjon be egy szamot!: "))
    szam2 = int(input("Kerem irjon be egy masik szamot is!: "))
    megoldas = (szam1 * szam2) * 2
    print("A teglalap keruletenek a vegeredmenye: ", megoldas, "kobmeter")

elif szamok == "Teglalap terulete":
    print("A Teglalap teruletenek a megoldokeplete: A * A ")
    print("Kerem adja meg az ertekeket meterben")
    szam1 = int(input("Kerem irja be az A erteket!: "))
    szam2 = int(input("Kerem adja meg a B erteket!: "))
    megoldas = szam1 * szam2
    print("A teglalap teruletenek a vegeredmenye: ", megoldas, "negyzetmeter")

elif szamok == "Haromszog kerulete":
    print("A Haromszog keruletenek a megoldokeplete: A * ma /2 ")
    print("Kerem adja meg az ertekeket meterben")
    szam1 = int(input("Adja meg az A erteket!: "))
    ma = int(input("Kerem adja meg a magassag erteket!: "))
    megoldas = szam1 * ma / 2
    print("A haromszog keruletenek a vegeredmenye: ", megoldas, "kobmeter")

elif szamok == "Haromszog terulete":
    print("A Haromszog teruletenek a megoldokeplete: A * B * C")
    print("Kerem adja meg az ertekeket meterben!")
    szam1 = int(input("Kerem irja be az A erteket!: "))
    szam2 = int(input("Kerem irja be a B erteket!: "))
    szam3 = int(input("Kerem irja be a C erteket!: "))
    megoldas = szam1 * szam2 * szam3
    print("A haromszog teruletenek vegeredmenye: ", megoldas, "negyzetmeter")

elif szamok == "Negyzet kerulete":
    print("A Negyzet keruletenek a megoldokeplete: A * B")
    szam1 = int(input("Irja be az A erteke kobmeterben!: "))
    megoldas = szam1 * szam1
    print("A negyzet keruletenek vegeredmenye: ", megoldas, "kobmeter")

elif szamok == "Negyzet terulet":
    print("A Negyzet teruletenek a megoldokeplete: A * 4 vagy A * A * A *A")
    szam1 = int(input("Kerem adja meg az A erteket meterben!: "))
    megoldas = szam1 * 4
    print("A negyzet teruletenek az vegeredmenye: ", megoldas, "negyzetmeter lett!")