#1
print("1 Harjutus")
print()
a=0
nimi_list=[] #Создание списка для будущего использования
for i in range(5):
    nimi=input("Kirjuta nimi ").title()
    while nimi.isalpha()==False:
        nimi=input("Kirjuta õige nimi ")
    nimi_list.append(nimi) #.append() В конец списка добавляется элемент, в данном случае введеная переменная добавляется в конец списка
nimi_list.sort() #.sort() Сортировка списка в порядка возрастания
print(nimi_list)
print("Viimane nimi on ", nimi)
print()

#2
print("2 Harjutus")
print()
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
print(opilased)
pos=input("Millist positsiooni tahaksid muuta? ")
while pos.isdigit()==False or int(pos)>5:
    pos=input("Kirjuta õige number! Millist positsiooni tahaksid muuta? ")
nimi=input("Kirjuta uus õpilane ")
while nimi.isalpha()==False:
    nimi=input("Kirjuta õige nimi ")
opilased.pop(int(pos)-1) #.pop(n) удаляет n элемент в списке
opilased.insert(int(pos)-1,nimi) #.insert(i,n) вставляет в i позицию, элемент n
print(opilased)
print()

#3
print("3 Harjutus")
print()
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
print(opilased)
x=i=len(opilased)
while i>=0:
    i-=1
    x=len(opilased)-1
    while x>=0 and i>=0:
        if x!=i and opilased[x]==opilased[i]:
            opilased.pop(x)
            if len(opilased)==i:
                i-=1
        x-=1
print(opilased)
print()

#4
print("4 Harjutus")
print()
vanus=[15,17,20,5,35,69,10,3,50,23]
print("vanuste nimekiri - ", vanus)
print("Kõige väiksem vanus - ", min(vanus))
print("Kõige suurem vanus - ", max(vanus))
keskmine=0
for i in range(0,len(vanus)):
    keskmine+=vanus[i]
print("Keskmine vanus - ", int(round(keskmine/len(vanus),0)), "or", keskmine/len(vanus))
print()

#5
print("5 Harjutus")
print()
numbrid=[1,5,2,23,12,2,7,9,1,5,3]
print(numbrid,"\n")
for i in range(0,len(numbrid)):
    print("* " * numbrid[i-1])
print()

#10 funktsioonid
print("10 funktsioonid")
while True:
    x=input(""" Palun vali funktsioon (1-10)
1 - Loendage märkide arv stringis
2 - Asendage mis tahes tähemärk
3 - Kontrollige, kas string sisaldab numbreid
4 - Kontrollige, kas string sisaldab tähti
5 - Kontrollige, kas kõik märgid on väiketähtedega
6 - Kontrollige, kas kõik märgid on suurtähtedega
7 - Kontrollige, kas 1 täht on suur ja ülejäänud väiketähtedega
8 - Muutke kõik tähed väikeseks
9 - Tehke kõik tähed suureks
10 - Tehke esimene täht suureks ja ülejäänud väikeseks
""")
    if x.isdigit()==False or int(x) not in range(1,11):
        continue
    x=int(x)
    print()
    text=input("Sisestage tekst, mille alusel soovite tegutseda\n")
    if x==1:
        print("Teksti pikkus - ",len(text)) # .len() показывает длину строки
    elif x==2:
        rep1=input("Mida asendada?\n")
        rep2=input("Millist sümbolit peaksin asendama?\n") 
        arv=input("Mitu korda vahetada?\n")
        while arv.isdigit()==False:
            arv=input("Kirjuta õige arv!\n")
        print("Uus text - ", text.replace(rep1,rep2,int(arv))) # .replace(x,y,i) заменяем x на y, i раз
    elif x==3:
        print("Kontrollige, kas tekst koosneb numbritest: ", text.isdigit()) # .isdigit() проверяем состоит ли строка лишь из цифр
    elif x==4:
        print("Kontrollige, kas tekst koosneb tähtedest: ", text.isalpha()) # .isalpha() проверяем состоит ли строка лишь из букв
    elif x==5:
        print("Kontrollige, kas tekst koosneb väiketähtedest: ", text.islower()) # .isdigit() проверяем состоит ли строка лишь из букв нижнего регистра
    elif x==6:
        print("Kontrollige, kas tekst koosneb suurtähtedest: ", text.isupper()) # .isupper() проверяем состоит ли строка лишь из буква верхнего регистра
    elif x==7:
        print("Kontrollige, kas 1 täht on suur ja ülejäänud on väikesed: ", text.istitle()) # .istitle() проверяем является ли 1 буква верхним регистром,
                                                                                            #а остальные нижним регистром
    elif x==8:
        print("Muutes kõik tähed väikeseks")
        print("Uus text - ", text.lower()) # .lower() делаем все буквы нижним регитром
    elif x==9:
        print("Muutes kõik tähed suurseks")
        print("Uus text - ", text.upper()) # .lower() делаем все буквы верхним регитром
    else:
        print("Tehke esimene täht suur ja ülejäänud väike")
        print("Uus text -", text.title()) # .title() делаем первую букву верхним регистром, а остальные нижним.
    vali=input("Kas soovite veel proovida (jah või ei)?\n").lower()
    while vali not in ["jah","ei"]:
        vali=input("Kirjutage ainult jah või ei\n").lower()
    if vali=="jah":
        continue
    else:
        break
# 1 len. 2 replace. 3 isdigit. 4 isalpha. 5 islower. 6 isupper. 7 istitle. 8 lower. 9 upper. 10 title.