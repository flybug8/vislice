a = ('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''')
b = ('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
c = ('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''')
d = ('''
  +---+
  |   |
  O   |
 /|  |
      |
      |
=========
''')
e = ('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
f = ('''
  +---+
  |   |
  O   |
 /|\  |
 /   |
      |
=========
''')
g = ('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========  

''')
h = ('''
  +---+
  |   |
  O   |
 /|\  |
 / \_  |
      |
========= 
''')
i = ('''
  +---+
  |   |
  O   |
 /|\  |
_/ \_  |
      |
=========
''')
j = ('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''')
k = ('''
  +---+
  |   |
  O   |
 \|/  |
  |    |   
_/ \_ |
      |
========= 
''')

print(
    Fore.RED, '''
    
██████╗░░█████╗░███████╗██████╗░██████╗░░█████╗░██╗░░░██╗██╗░░░░░░░░░░██╗███████╗███╗░░██╗
██╔══██╗██╔══██╗╚════██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░░░░░░██║██╔════╝████╗░██║
██████╔╝██║░░██║░░███╔═╝██║░░██║██████╔╝███████║╚██╗░██╔╝██║░░░░░░░░░░██║█████╗░░██╔██╗██║
██╔═══╝░██║░░██║██╔══╝░░██║░░██║██╔══██╗██╔══██║░╚████╔╝░██║░░░░░██╗░░██║██╔══╝░░██║╚████║
██║░░░░░╚█████╔╝███████╗██████╔╝██║░░██║██║░░██║░░╚██╔╝░░███████╗╚█████╔╝███████╗██║░╚███║
╚═╝░░░░░░╚════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚══════╝╚ 
                                        ██╗░░░██╗
    avtor : gal bodiroza                ██║░░░██║
                                        ╚██╗░██╔╝            
                                        ░╚████╔╝░
                                        ░░╚██╔╝░░
                                        ░░░╚═╝░░░         
                              ██╗░██████╗░██████╗░░█████╗░
                              ██║██╔════╝░██╔══██╗██╔══██╗
                              ██║██║░░██╗░██████╔╝██║░░██║
                              ██║██║░░╚██╗██╔══██╗██║░░██║
                              ██║╚██████╔╝██║░░██║╚█████╔╝
                              ╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░
''')
print(Fore.WHITE)


def imena():
    ime = input("Ime prvega  igralca: ")
    ime1 = input("Ime drugega igralca: ")
    print(
        "Pozdravljena v igro!!! , " + ime,
        " in " + ime1,
    )
    print("  -  -  -  ")


imena()

beseda = str.lower(input("Drugi igralec naj vnese besedo: "))
list = []

for x in range(0, len(beseda)):
    list.append(beseda[x])
this = str(len(list))
print("Beseda ima %s črk." % (this))
print("Loading...")
print(".. .. .. .. .. ..")
print("Začni z ugibanjem...")
ugibi = ''

poizkus = 10

while poizkus > 0:
    nepravilno = 0
    for char in beseda:
        if char in ugibi:
            print(char)
        else:
            print("_"),
            nepravilno += 1
    if nepravilno == 0:
        print(Fore.CYAN, "Zmaga!!!")
        print(Fore.WHITE, k)

        break
    print

    ugib = input("Ugani besedo:")
    ugibi += ugib
    if ugib not in beseda:
        poizkus -= 1
        if poizkus == 9:
            print(a)
        elif poizkus == 8:
            print(b)
        elif poizkus == 7:
            print(c)
        elif poizkus == 6:
            print(d)
        elif poizkus == 5:
            print(e)
        elif poizkus == 4:
            print(f)
        elif poizkus == 3:
            print(g)
        elif poizkus == 2:
            print(h)
        elif poizkus == 1:
            print(i)

        print(Fore.RED, "Narobe")
        print(Fore.WHITE, "Imas se", +poizkus, 'poiskusov')
        if poizkus == 0:
            print("Izgubil si")
            print(j)
            print("Rešitev: %s ." % (beseda))

