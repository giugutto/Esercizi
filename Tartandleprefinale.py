import random

def print_quadri(position, lepre_pos, tartaruga_pos):
    for i in range(1, 71):
        if i == tartaruga_pos:
            print("T", end=" ")
        elif i == lepre_pos:
            print("H", end=" ")
        elif i == lepre_pos and i == tartaruga_pos:
            print("OUCH!", end=" ")
        else:
            print("-", end=" ")
    print()

#ogni 10 tick dell'orologio.
def tartaruga_move(weather, energy) -> int:
    x = random.randint(1, 10)
    passoveloce = 3
    passolento = -6
    scivolata = 1
    if weather == "Pioggia": 
        x -= 1
    if x <= 5:
        if energy >= 5:
            energy -= 5
            return passoveloce, energy
        else:
            energy += 10
            return 0, energy
    elif x <= 7:
        if energy >= 10:
            energy -= 10
            return scivolata, energy
        else:
            energy += 10
            return 0, energy    
    else:
        if energy >= 3:
            energy -= 3
            return passolento, energy
        else:
            energy += 10
            return 0, energy    
    

def lepre_move(weather, energy):
    i = random.randint(1,10)
    grandeb = 9
    grandes = -12
    piccolob = 1
    piccolas = -2
    if weather == "Pioggia":
        i -= 2 
    if i <= 2:
        energy = min(100, energy + 10)
        return 0, energy
    if i <= 4:
        if energy >= 15:
            energy -= 15
            return grandeb, energy
        else:
            return 0, energy
    if i <= 5:
        if energy >= 20:
            energy -= 20
            return grandes, energy
        else:
            return 0, energy
    if i <= 8:
        if energy >= 5:
            energy -= 5
            return piccolob, energy
        else:
            return 0, energy
    if i <= 11:
        if energy >= 8:
            energy -= 8
            return piccolas, energy
        else:
            return 0, energy
        
       
def change_weather(tick):
    if tick % 10 == 0:
        return random.choice(["soleggiato", "pioggia"])
    else:
        return None

print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

lepre_pos = 1
tartaruga_pos = 1

tartaruga_energia = 100
lepre_energia = 100

tick = 0
weather = "soleggiato"

while True:
    tick += 1
    weather = change_weather(tick) or weather #se non c'è nessun cambiamento lascia il meteo corrente
    Ostacoli:dict = {15: -3, 30: -5, 45: -7}
    Bonus:dict = {10: 5, 25: 3, 50: 10}
    lepre_move_result, lepre_energia = lepre_move(weather, lepre_energia)
    lepre_pos += lepre_move_result

    for k,v in Ostacoli.items():
        if lepre_pos == k:
            lepre_pos -= v
        else:
            continue
    for k,v in Bonus.items():
        if lepre_pos == k:
            lepre_pos += v
        else:
            continue
    if lepre_pos < 0:
        lepre_pos = 0
    tartaruga_move_result, tartaruga_energia = tartaruga_move(weather, tartaruga_energia)
    tartaruga_pos += tartaruga_move_result
    for k,v in Ostacoli.items():
        if tartaruga_pos == k:
            tartaruga_pos -= v
        else:
            continue
    for k,v in Bonus.items():
        if tartaruga_pos == k:
            tartaruga_pos += v
        else:
            continue
    if tartaruga_pos < 0:
        tartaruga_pos = 0

    print_quadri(70, lepre_pos,tartaruga_pos)

    if lepre_pos >= 70 and tartaruga_pos >= 70:
        print("IT'S A TIE!!")
        break
    elif lepre_pos >= 70:
        print("LEPRE WINS || YUCH!!")
        break
    elif tartaruga_pos >= 70:
        print("TARTARUGA WINS! || VAY!")
        break




Ostacoli:dict = {15: -3, 30: -5, 45: -7}

Bonus:dict = {10: 5, 25: 3, 50: 10}