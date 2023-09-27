def main():
   print('''Hello, I am your personal birthday reminder.
    Enter the name of the person which you wanna know when the birthday is and year is it now, with this i can determine  
   the age of a person !(Write name in lower case)!  ''')
   print('''If you wanna find out person's bd, type 'name', if you wanna find bd in certain month type 'group m'
or certain group of people type 'group g' ''')

answear_ = str(input())

year_ = int(input("Enter what year it is\n"))
erik = "Erik's birthday is 13 October and his age in this year is {}".format(year_ - 2004)
mom = "Mom's birthday is 11 September and his age in this year is {}".format(year_ - 1975)
dad = "Dad's birthday is 21 October and his age in this year is {}".format(year_ - 1976)
vlad = "Vlad's birthday is 24 September and his age in this year is {}".format(year_ - 1999)
vadya = "Vadya's birthday is 3 June and his age in this year is {}".format(year_ - 2009)
serega = "Serega's birthday is 20 June and his age in this year is {}".format(year_ - 2005)
albina = "Albina's birthday is 13 October and his age in this year is {}".format(year_ - 2007)  # fff
gf_petro = "Grandpa Petro's birthday is 26 March and his age in this year is {}".format(year_ - 1953)
gf_kolya = "Grandpa Kolya's birthday is 13 August and his age in this year is {}".format(year_ - 1954)
gm_m = "Grandma Tanya's birthday is 28 October and his age in this year is {}".format(year_ - 1953)
gm_f = "Grandma Tanya's birthday is 3 October and his age in this year is {}".format(year_ - 2004)
uncle = "Uncle Micha's birthday is 21 October and his age in this year is {}".format(year_ - 2004)  # fff
aunt = "Aunt Rita's birthday is 4 April and his age in this year is {}".format(year_ - 1983)
vova = "Vova's birthday is 30 July and his age in this year is {}".format(year_ - 2004)
danya_kpi = "Danya's birthday is 6 December and his age in this year is {}".format(year_ - 2004)
sasha_kpi = "Sasha's birthday is 11 July and his age in this year is {}".format(year_ - 2004)
oleksei_kpi = "Lesa's birthday is 29 March and his age in this year is {}".format(year_ - 2004)
tanya_kpi = "Tanya's birthday is 15 November and his age in this year is {}".format(year_ - 2004)
viktor_kpi = "Viktor's birthday is 1 November and his age in this year is {}".format(year_ - 2004)
kostya_kpi = "Kostya's birthday is 3 November and his age in this year is {}".format(year_ - 2004)
alina_kpi = "Alina's birthday is 29 December and his age in this year is {}".format(year_ - 2004)
sanya_kpi = "Sanya's birthday is 2 September and his age in this year is {}".format(year_ - 2004)
dashya_kpi = "Dashya's birthday is 12 April and his age in this year is {}".format(year_ - 2004)

group_ = [erik.split(), mom.split(), dad.split(), vlad.split(), vadya.split(), serega.split(), albina.split(),
          gf_petro.split(), gf_kolya.split(), gm_m.split(), gm_f.split(), uncle.split(), aunt.split(), vova.split(),
          danya_kpi.split(), sasha_kpi.split(), oleksei_kpi.split(), tanya_kpi.split(), viktor_kpi.split(),
          kostya_kpi.split(), alina_kpi.split(), sanya_kpi.split(),  dashya_kpi.split()]

group_family = [dad, mom, vlad, vadya]
group_kpi = [danya_kpi, sasha_kpi, oleksei_kpi, tanya_kpi, viktor_kpi, kostya_kpi, alina_kpi, sanya_kpi, dashya_kpi]
group_frl = [vova, erik]

def names():
    print("If you wanna again find person - type 'group', if wanna stop program type 'stop' and if you want retuen"
          "back and choose another category type 'rtn' ")
    print("Ok, lets find this person's birthday")
    while True:
        name_ = str(input("\nEnter the name of the person\n"))
        if name_ == 'erik':
            print(erik)
        elif name_ == 'mom':
            print(mom)
        elif name_ == 'dad':
            print(dad)
        elif name_ == 'vlad':
            print(vlad)
        elif name_ == 'vadya':
            print(vadya)
        elif name_ == 'serega':
            print(serega)
        elif name_ == 'albina':
            print(albina)
        elif name_ == 'gf_petro':
            print(gf_petro)
        elif name_ == 'gf_kolya':
            print(gf_kolya)
        elif name_ == 'gm_m':
            print(gm_m)
        elif name_ == 'gm_f':
            print(gm_f)
        elif name_ == 'uncle':
            print(uncle)
        elif name_ == 'aunt':
            print(aunt)
        elif name_ == 'vova':
            print(vova)
        elif name_ == 'danya_kpi':
            print(danya_kpi)
        elif name_ == 'sasha_kpi':
            print(sasha_kpi)
        elif name_ == 'oleksei_kpi':
            print(oleksei_kpi)
        elif name_ == 'tanya_kpi':
            print(tanya_kpi)
        elif name_ == 'viktor_kpi':
            print(viktor_kpi)
        elif name_ == 'kostya_kpi':
            print(kostya_kpi)
        elif name_ == 'alina_kpi':
            print(alina_kpi)
        elif name_ == 'sanya_kpi':
            print(sanya_kpi)
        elif name_ == 'dashya_kpi':
            print(dashya_kpi)
        elif name_ == 'group':
            return groupm()
        elif name_ == 'stop':
            break
        elif name_ == 'rtn':
            main()
        else:
            print("This person isn't in my base, try again or look in base")

def groupg():
    choose_g = str(input("Choose group which you wanna known(groupf(family), groupk(kpi), groupff(friend)\n"))
    if choose_g == 'groupf':
        for i in group_family:
            print(i, end='\n')
    elif choose_g == 'groupk':
        for i in group_kpi:
            print(i, end='\n')
    elif choose_g == 'groupff':
        for i in group_frl:
            print(i, end='\n')


def groupm(choose_=True):
    print("If you wanna again find person - type 'names', if wanna stop program type 'stop' ")
    while choose_:
        month_ = str(input("\nWhich month you wanna know? (Type in low register and type first 3 world)\n"))
        for i in group_:
            for y in i:
                if month_ == 'jan':
                    if 'January' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'feb':
                    if 'February' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'mar':
                    if 'March' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'apr':
                    if 'April' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'may':
                    if 'May' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'jun':
                    if 'June' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'jul':
                    if 'July' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'aug':
                    if 'August' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'sep':
                    if 'September' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'oct':
                    if 'October' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'nov':
                    if 'November' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'dec':
                    if 'December' in y:
                        print(" ".join(i), end='\n')
                elif month_ == 'names':
                    return names()
                elif month_ == 'stop':
                    choose_ = False
                else:
                    print("This month isn't in my base, try again or look in base")


if answear_ == 'name':
     names()
elif answear_ == 'group m':
     groupm()
elif answear_ == 'group g':
    groupg()

massive = []
for i in massive:
    massive.append([])
    for w in i:
        r = randint(0, 99)
        