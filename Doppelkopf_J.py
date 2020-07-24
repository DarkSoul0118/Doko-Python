import random


class Spieler():
    def __init__(self, hand, anspieler, partei):
        pass
        self.hand = hand
        self.anspieler = anspieler
        self.partei = partei
"""
    def __str__(self):
        result = ""
        for index, card in enumerate(self.hand):
            result += str(index+1) + ":" + card.name + "  "
        return result
"""
class Stich():
    def __init__(self, mittelpile, anspiel, winner, punkte):
        self.mittelpile = mittelpile
        self.anspiel = anspiel
        self.winner = winner
        self.punkte = punkte

class Karte():
    def __init__(self, color, value, trump, order):
        self.color = color
        self.value = value
        self.trump = trump
        self.order = order
        self.name = "[" + color + " " + value + "]"

re_Punkte = 0
contra_Punkte = 0

# Kreuz
KA = Karte("♣", "A", False, 13)
K10 = Karte("♣", "10", False, 14)
KK = Karte("♣", "K", False, 15)
KD = Karte("♣", "D", True, 2)
KJ = Karte("♣", "J", True, 6)

# Pik
PA = Karte("♠", "A", False, 16)
P10 = Karte("♠", "10", False, 17)
PK = Karte("♠", "K", False, 18)
PD = Karte("♠", "D", True, 3)
PJ = Karte("♠", "J", True, 7)

# Herz
HA = Karte("♥", "A", False, 19)
H10 = Karte("♥", "10", True, 1)
HK = Karte("♥", "K", False, 20)
HD = Karte("♥", "D", True, 4)
HJ = Karte("♥", "J", True, 8)

# Caro
CA = Karte("♦", "A", True, 10)
C10 = Karte("♦", "10", True, 11)
CK = Karte("♦", "K", True, 12)
CD = Karte("♦", "D", True, 5)
CJ = Karte("♦", "J", True, 9)

Alle_Karten = [KA, K10, KK, KD, KJ, PA, P10, PK, PD, PJ, HA, H10, HK, HD, HJ, CA, C10, CK, CD, CJ,
               KA, K10, KK, KD, KJ, PA, P10, PK, PD, PJ, HA, H10, HK, HD, HJ, CA, C10, CK, CD, CJ]



random.shuffle(Alle_Karten)

Hands = [
    [],
    [],
    [],
    []
]


for Hand in Hands:
    for i in range(0, 10):
        c = Alle_Karten.pop()
        Hand.append(c)
    Hand.sort(key=lambda x: x.order, reverse = False)


Spieler_1 = Spieler(Hands[0], False, "Contra")
Spieler_2 = Spieler(Hands[1], False, "Contra")
Spieler_3 = Spieler(Hands[2], False, "Contra")
Spieler_4 = Spieler(Hands[3], False, "Contra")

Alle_Spieler = [
    Spieler_1,
    Spieler_2,
    Spieler_3,
    Spieler_4
]
def fall(Karte):
    if Karte.trump == True:
        return "T"
    else:
        return Karte.color

def partei_auswählen(Hand):
    for Karte in Hand:
        if Karte == KD:
            return True
            break

def parteien_auswählen():
    for spieler in Alle_Spieler:
            if partei_auswählen(spieler.hand):
                spieler.partei = "Re"

def checker(hand, stich, gespielte_Karte):
    if stich.anspiel == "T":
       if fall(gespielte_Karte) == "T":
        return True
       elif farbchecker(hand, "T") == False:
           return True
       else:
           return False
    if stich.anspiel == "♣":
       if fall(gespielte_Karte) == "♣":
        return True
       elif farbchecker(hand, "♣") == False:
           return True
       else:
           return False
    if stich.anspiel == "♠":
       if fall(gespielte_Karte) == "♠":
        return True
       elif farbchecker(hand, "♠") == False:
           return True
       else:
           return False
    if stich.anspiel == "♥":
       if fall(gespielte_Karte) == "♥":
        return True
       elif farbchecker(hand, "♥") == False:
           return True
       else:
           return False

def farbchecker(hand, case):
    if case == "T":
        for Karte in hand:
            if fall(Karte) == "T":
                return True
        else:
            return False
    else:
        for Karte in hand:
            if Karte.color == case and Karte.trump == False:
                return True
        else:
            return False

def zaehler(zu_Zaehlende_Karten):
    punktzahl = 0
    for Karte in zu_Zaehlende_Karten:
        if Karte.value == "A":
            punktzahl += 11
        elif Karte.value == "10":
            punktzahl += 10
        elif Karte.value == "K":
            punktzahl += 4
        elif Karte.value == "D":
            punktzahl += 3
        elif Karte.value == "J":
            punktzahl += 2
    return punktzahl

def anspieler(spielerArray):
    for index, spieler  in enumerate(spielerArray):
        if spieler.anspieler:
            return index+1

def setTrump(t):
    if t == "Normalspiel":
        Trump = [H10, HD, KD, CD, PD, HJ, KJ, CJ, PJ, CA, C10, CK]
    elif t == "Fleischlos":
        Trump = []
    elif t == "Damensolo":
        Trump = [HD, KD, CD, PD]
    elif t == "Bubensolo":
        Trump = [HJ, KJ, CJ, PJ]
    elif t == "Kreuzsolo":
        Trump = [KA, K10, KK, KD, KJ]
    elif t == "Karosolo":
        Trump = [CA, C10, CK, CD, CJ]
    elif t == "Herzsolo":
        Trump = [HA, H10, HK, HD, HJ]
    elif t == "Piksolo":
        Trump = [PA, P10, PK, PD, PJ]

def winner(mittelpile, spielerArray):
    order_Der_Karten = []

    if farbchecker(mittelpile, "T"):
        for Karte in mittelpile:
            order_Der_Karten.append(Karte.order)
            print("Test")
        order_Der_Karten.index(min(order_Der_Karten))
        spielerzahl = anspieler(spielerArray)
        indexPlusSpielerzahl = spielerzahl + order_Der_Karten.index(min(order_Der_Karten))
        print("Test")
        if indexPlusSpielerzahl < 4:
            print("Durchgelaufen")
            return indexPlusSpielerzahl - 4
    else:
        indexPlusSpielerzahl = 1
        print("Durchfall")
        return indexPlusSpielerzahl

    Testhand = [H10, K10, C10, KD]
    print(winner(Testhand, Alle_Spieler))





Testhand = [H10, H10, PD, HD]


"""
Testmittelpile = []
Teststich = Stich(Testmittelpile,KA.color,True,30)
Testhand = [H10, KD, PD, HD]
Test2 = []
print(checker(Testhand,Teststich,KK))
print(farbchecker(Testhand, ""))
print(Spieler_1)
"""
#Turn Cycle
#for i in range(0,10)
#    for player in Alle_Spieler:
#        #player legt Karte
#    if checker:
#        continue
#    else: #player verliert
##Winner Funktion