# 4 / 1. Írjon programot, ami valós számként bekéri az alábbi három adatot:
# a.    egy autó fogyasztását (liter/100km),
# b.    egy liter üzemanyag árát,
# c.    azt, hogy hány kilométert utaztunk az autóval
# Ezt követően írja ki két tizedesjegyre kerekítve, hogy az adott utazás hány forintba került az autóval! Ha bármelyik érték bekérése során negatív szám érkezik, akkor írjuk ki: Hibás adat, kezdje újra!, és a program álljon le, a következő értéket már ne kérje be, illetve az utolsó!
# Bekérjük az autó fogyasztását liter/100km-ben
# fogyasztas = float(
#     input("Kérem adja meg az autó fogyasztását (liter/100km): "))

# # Ellenőrizzük, hogy a fogyasztás pozitív-e
# if fogyasztas <= 0:
#     print("Hibás adat, kezdje újra!")
# else:
#     # Bekérjük a liter üzemanyag árát
#     ar = float(input("Kérem adja meg a liter üzemanyag árát: "))

#     # Ellenőrizzük, hogy az ár pozitív-e
#     if ar <= 0:
#         print("Hibás adat, kezdje újra!")
#     else:
#         # Bekérjük az utazott kilométerek számát
#         tavolsag = float(
#             input("Kérem adja meg, hány kilométert utazott az autóval: "))

#         # Ellenőrizzük, hogy a távolság pozitív-e
#         if tavolsag <= 0:
#             print("Hibás adat, kezdje újra!")
#         else:
#             # Számoljuk ki az utazás költségét
#             koltseg = (tavolsag / 100) * fogyasztas * ar

#             # Kiírjuk az eredményt két tizedesjegyre kerekítve
#             print("Az utazás költsége: {:.2f} forint".format(koltseg))

# 2.	Írjon programot, ami bekér egy háromjegyű számot! A programba csak háromjegyű szám írható be, ellenkező esetben adjon hibaüzenetet és kérje be a számot addig, amíg megfelelő szám nem érkezik! Ha megfelelő számot írt be a felhasználó, írjuk ki a számot szöveggel! Ha olyan számot ad a felhasználó, amelynek minden számjegye egyezik, írjuk ki a mágikus szám! szöveget! 

# be_szam="0"
# while len(be_szam)!=3:
#     be_szam=input("Kérek egy három számjegyű számot: ") or "123"

# egyesek=["egy","kettő","három","négy","öt","hat","hét","nyolc","kilenc","tíz"]
# tizesek=["tizen","huszon","harminc","negyven","ötven","hatvan","hetven","nyolcvan","kilencven"]
# szazasok=["száz","kétszáz","háromszáz","négyszáz","ötszáz","hatszáz","hétszáz","nyolcszáz","kilenczszáz"]

# szam=int(be_szam)
# print(szazasok[(szam//100)-1])
# szam%=100
# if szam//10==1 and szam%10==0:
#     print("tíz")
# elif szam//20==1 and szam%10==0:
#     print("húsz")
# else:
#     print(tizesek[szam//10-1])
# szam%=10
# print(egyesek[szam-1])

# if be_szam[0]==be_szam[1] and be_szam[1]==be_szam[2]:
#     print("A szám mágikus!")

# 3.	A mellékelt paszuly.txt szövegfájban az Égig érő paszuly című mese olvasható. Olvassa be a szövegfájlt tartalmát egy erre alkalmas adatszerkezetbe, majd oldja meg az alábbi feladatokat:
# a.	Írja ki a képernyőre, hány sort olvasott be a fájlból!
# b.	Írja ki, hogy a mese hány mondatból áll! (Minden mondat végén pont, kérdőjel vagy felkiáltójel található.) 
# c.	Hányféle ragozott formában fordul elő a paszuly szó a szövegben? Gyűjtse össze és írja ki az összes ragozott formát! Ügyeljen arra, hogy egy szót csak egyszer jelenítsen meg és a szavak ne tartalmazzák az őket követő írásjeleket (; , . ! ?)
# d.	Írja ki, melyik a legrövidebb sor a fájlban (melyik sor tartalmazza a legkevesebb karaktert)! Jelenítse meg magát a sort és karaktereinek számát is!


# mese=[]
# with open("paszuly.txt", "r", encoding="utf-8") as fin:
#     for sor in fin:
#         mese.append(sor.strip())

# print(f"{len(mese)} sort olvastunk be a fájlból.")

# mondatok_szama = 0
# for sor in mese:
#     mondatok_szama+=sor.count(".")+sor.count("?")+sor.count("!")
    
# print(f"A mese {mondatok_szama} mondatból áll.")

# ragozott_alakok = []
# for sor in mese:
#     szavak = sor.replace(".", "").replace(";", "").replace(",", "").replace("?", "").replace("!","").split()
#     for szo in szavak:
#         if "paszuly" in szo and szo not in ragozott_alakok:
#             ragozott_alakok.append(szo)

# print("A paszuly ragozott formái:")
# for szo in ragozott_alakok:
#     print(szo)


# min_index=0
# for i in range(1,len(mese)):
#     if len(mese[i])<len(mese[min_index]):
#         min_index=i

# print("A legrövidebb sor:")
# print(mese[min_index])
# print("Karaktereinek száma:",len(mese[min_index]))
