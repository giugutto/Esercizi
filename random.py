#Scrivi una funzione che accetta una stringa come input,
#rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi sono parole
#univoche nel testo rimanente (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura)
#e i valori sono le frequenze di quelle parole.

#For example: stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
#text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
#print(word_frequency(text, stopwords))


from collections import Counter
def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    x = text.split()
    for i in x:
        if i in stopwords:
            x.remove(i)
        else:
            continue
    a = Counter(x)

    return a
    


print(word_frequency("The quick brown fox jumps over the lazy dog. The dog is very lazy.",['the', 'and', 'is', 'in', 'on', 'of']))
