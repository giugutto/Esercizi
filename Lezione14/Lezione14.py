#UNITTESTING

#keyword: assert, pytest
#nel caso il test non sarà eseguito, assert lancia un'eccezione
#esempio
def sum_positive_numbers(a, b):
    assert a >= 0 and b>=0, 'sbagliato'
    return a + b


