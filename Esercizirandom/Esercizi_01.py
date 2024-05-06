# Scrivete una espressione che calcoli il numero di secondi che ci sono in
# 42 minuti e 42 secondi.
s = 42 * 60 + 42
print(s)


# Scrivete una espressione che calcoli il numero di miglia che ci sono in
# 10 chilometri. (1 miglio=1.61 km).
miglia = 10 / 1.61
print(miglia)


# Scrivete una espressione che calcoli la velocità media e la cadenza media
# (tempo per miglio, in minuti e secondi) di un corridore che corre una gara
# di 10 chilometri in 42 minuti e 42 secondi.

s = 42 * 60 + 42
miglia = 10 * 1.61
metri = 10 
v = metri/s
c = miglia/s
print(c, v)

# Il volume di una sfera di raggio `r` è `4/3 * PI * r ^ 3`.
# Scrivere una espressione che calcoli il volume di una sfera di raggio 5.
r = 5
volume = 4/3 * 3.14 * r ** 3

print(volume)


# Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40%
# di sconto. I costi di spedizione sono 3 euro per la prima copia, e 75
# centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?

copertina = 24.95
#sconto = 40% 
#shipping = 3
copies = 0.75 

sconto = copertina * 40 / 100
costolibro = copertina - sconto
v = copies * 59 + 3
costot = costolibro * 60 + v
print(costot)

# Se uscite di casa alle 6: 52 di mattina e correte un miglio a ritmo blando
# (8 minuti e 15 secondi al miglio), e poi 3 miglia a ritmo moderato
# (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando
# (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?

primom = 8 * 60 + 15
trem = 3 * (7 * 60 + 12)
ultim = 9 * 60 + 45

secondi = primom + trem + ultim

orario = 360 * 60 + 52 * 60

orariorit = (secondi + orario) / 60 

orarioit2 = orariorit / 60
min = (orarioit2 % 1) * 60
ore = orarioit2 // 1

print(f"{int(ore)}:{int(min)}")


# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale.
# Ad esempio, `s = "85721"`. Stampate la somma delle cifre contenute nella stringa.

# s = "45642"
# a = tuple(s)

# print(sum(a))
# Scrivete una espressione che a partire da una stringa di 5 caratteri,
# rappresentante un numero binario, stampi la sua rappresentazione decimale.
# Ad esempio, `s = "00101" -> 5`.


binarynum = "01001"
decnum = int(binarynum, 2)
print(decnum)

# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale
# ('.'). Ad esempio, s = "52.29". Stampare il numero decimale rappresentato
# dalla stringa(stamparlo come numero, non come stringa).
numeros = "52.29"
print(float(numeros))


# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.

def virgola(v: float) -> float:
    c = s **3
    return c

virgola(32.45)
# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e ritorna la maggiore.
# Modificare poi la funzione per ritornare entrambi i valori.

def rad(a,b,c):
    ris = b**2 - 4

#b^2 - 4 ac


# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e le ritorna entrambe.
#def rad(a:float, b:float, c:float):



# Scrivere una funzione che prende come input cinque numeri e ritorna la somma
# dei numeri pari meno quella dei numeri dispari.

def pardir(a,b,c,d,e):
    listpar= []
    listdis = []
    x = a,b,c,d,e
    for i in x:
        if a % 2 == 0:
            listpar.append(i)
        else:
            listdis.append(i)
    p = sum(listpar)
    d_1 = sum(listdis)
    return p - d_1
print(pardir(3,6,2,8,1))


# Scrivere una funzione che prende tre valori di input, e ritorna la
# loro somma se i valori sono punteggi di esame validi(`0 <= grade <= 30`),
# e altrimenti ritorna `- 1`. Scriverne poi una variante che legge i valori da
# terminale con `input`.
def esame(a,b,c):
    x = sum(a,b,c)
    if 0<x<30:
        print(x)
    else:
        print("-1")
 #####################
def esame(a = None,b = None,c = None):
    a = input("Scrivi primo valore")
    b = input("Scrivi secondo valore")
    c = input("Scrivi terzo valore")
    x = sum(a,b,c)
    if 0<x<30:
        print(x)
    else:
        print("-1")

# Scrivere una funzione che prende tre valori(`d`, `m`, `y`) e ritorna se la
# data è valida o no. Si possono ignorare gli anni bisestili. Ad esempio,
# ritorna `False` per `30/2/2017` e `True` per `1/1/1111`.

def annov(d,m,y):
    if 1<=d<=31 and 1<=m<=12 and 0<=y<=5000:
        return True
    else:
        return False
    
print(annov(10,8,2021))

# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`.
def strip(x):
    fin = x.replace(" ", "")
    return fin
print(strip("  ciao   "))

# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome letto come input e poi da `Buona giornata!`

def saluto(nome):
    return (f"ciao {nome} buonagiornata!")

print(saluto("Peppe"))