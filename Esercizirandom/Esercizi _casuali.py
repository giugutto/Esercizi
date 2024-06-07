#Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.
quadrato_tuple: tuple = tuple(i ** 2 for i in range(1, 6))
print(quadrato_tuple)
#Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".
tup = ("mela","banana","kiwi")

print(tup[1])
#Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

varcon = 0
for i in tup:
    if i == "mela":
        varcon += 1
    else:
        continue

print(varcon)