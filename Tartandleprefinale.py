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


def tartaruga_move(weather, energy) -> int:
    x = random.randint(1, 10)
    passoveloce = 3
    passolento = -6
    scivolata = 1
    if x <= 5:
        if energy >= 5:
            energy -= 5
            if weather == "Pioggia":
                return passoveloce -1, energy
            return passoveloce, energy
        else:
            energy += 10
            return 0, energy
    elif x <= 7:
        if energy >= 10:
            energy -= 10
            if weather == "Pioggia":
                return scivolata -1, energy
            return scivolata, energy
        else:
            energy += 10
            return 0, energy    
    else:
        if energy >= 3:
            energy -= 3
            if weather == "Pioggia":
                return passolento -1, energy
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
    
    if i <= 2:
        energy = min(100, energy + 10)
        return 0, energy
    if i <= 4:
        if energy >= 15:
            energy -= 15
            if weather == "Pioggia":
                return grandeb -2, energy
            return grandeb, energy
        else:
            return 0, energy
    if i <= 5:
        if energy >= 20:
            energy -= 20
            if weather == "Pioggia":
                return grandes -2, energy
            return grandes, energy
        else:
            return 0, energy
    if i <= 8:
        if energy >= 5:
            energy -= 5
            if weather == "Pioggia":
                return piccolob -2, energy
            return piccolob, energy
        else:
            return 0, energy
    if i <= 11:
        if energy >= 8:
            energy -= 8
            if weather == "Pioggia":
                return piccolas -2, energy
            return piccolas, energy
        else:
            return 0, energy
        
#ogni 10 tick dell'orologio.    
def change_weather(tick):
    if tick % 10 == 0:
        return random.choice(["soleggiato", "Pioggia"])
    else:
        return None

print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

lepre_pos = 1
tartaruga_pos = 1

tartaruga_energia = 100
lepre_energia = 100

tick = 0
weather = "soleggiato"
Ostacoli:dict = {15: -3, 30: -5, 45: -7}
Bonus:dict = {10: 5, 25: 3, 50: 10}

while True:
    tick += 1
    weather = change_weather(tick) #or weather #se non c'è nessun cambiamento lascia il meteo corrente
    lepre_move_result, lepre_energia = lepre_move(weather, lepre_energia)
    lepre_pos += lepre_move_result
    if lepre_pos < 0:
        lepre_pos = 0
    for k,v in Ostacoli.items():
        if lepre_pos == k:
            lepre_pos += v
        else:
            continue
    for k,v in Bonus.items():
        if lepre_pos == k:
            lepre_pos += v
        else:
            continue
    tartaruga_move_result, tartaruga_energia = tartaruga_move(weather, tartaruga_energia)
    tartaruga_pos += tartaruga_move_result
    if tartaruga_pos < 0:
        tartaruga_pos = 0
    for k,v in Ostacoli.items():
        if tartaruga_pos == k:
            tartaruga_pos += v
        else:
            continue
    for k,v in Bonus.items():
        if tartaruga_pos == k:
            tartaruga_pos += v
        else:
            continue
    

    print_quadri(70, lepre_pos,tartaruga_pos)

    if lepre_pos >= 70 and tartaruga_pos >= 70:
        print("IT'S A TIE!!")
        break
    elif lepre_pos >= 70:
        print("LEPRE WINS || YUCH!!")
        break
    elif tartaruga_pos >= 70:
        print("TARTARUGA WINS! || YAY!")
        break




