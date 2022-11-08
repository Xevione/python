#def add(x,y) ---> return addition
def add(x,y):
    return (x + y)



#def sub(x,y) ---> return soustraction
def sub(x,y):
    return (x - y)


#def multiply(x,y) ---> return multiplication
def multiply(x,y):
    return (x * y)


#def divide(x,y) ---> return  division
def divide(x,y):
    #Si y est égale a zéro
    if y ==0:
    #Alors on affiche que ce n'est pas possible
        print('pas possible')
    #Sinon, pas de probleme
    else:
    #on divise le premier element par le deuxieme
        return (x / y)


#def modulo(x,y) ---> return modulo
def multiply(x,y):
    return ( x % y)



#Calculer le salaire:

def calculSalairParSeconde(salaireHoraire, HeureParJourOuvrable,JourOuvrable):
    salairAnnuel = salaireHoraire * HeureParJourOuvrable * JourOuvrable # Je calcule le salaire annuel
    nbSeconde = 365 * 24 * 60 * 60 # Je calcul le nombre de secondes dans une année
    return salairAnnuel / nbSeconde # Je divise le salaire annuel par le nombre de seconde par an
    #return((salaireHoraire*HeureParJourOuvrable*JourOuvrable)/(365*24*60*60))

def withdrawFees(total,percent):
    #calcul du montant des taxes a retirer
    fees = total * (percent/100)
    #Je retourne mon total sans les taxes
    return total - fees

def calculeSalaireNet(salairBrut, public):
    #Si j'occupe un poste de la fonction publique
    if public:
    #Alors je retourne le salaire brut - 15% de taxe
        return withdrawFees(salairBrut, 15)
    #Sinon, c'est que je suis un travailleur privé,
    else:
    #Alors je retourne le salaire brut - 23% de grosse taxe sa mère
        return withdrawFees(salairBrut, 23)

#def calculSalaireNet(SalairBrut):
    #Je calcule le salaire net
    #SalairNet = SalairBrut * 0.77
    #Je renvoie le salair net
    #return SalairNet