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
        return
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

tour = 0
# Tant que je ne suis pas au tour 5
while tour != 5 :
# Appeler la fonction JouerUnTour
# J'effectue l'action de passer un tour
    tour = tour + 1



#Exercice:
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere
    # le caractere doit etre parametrable
def devine(x):
    #nombre de tentative
    tenta = 0
    # Je definie une variable char qui permet de contenir le caracère genere avec input
    char = None
    #Tant que l'input de la lettre n'est pas egal au caractere string au hasard ou tentative > 10 alors
    while (char!= x) :
         #Je redéfinis la variable char par un caractere genere au hasard avec input
        char = input()
        #J'incremente la variable tenta
        tenta = tenta + 1
    # J'affiche le nombre de tentatives
    print(tenta)

       

def miniGame(winCondition):
    # Je definie une variable char qui permet de contenir le caracère genere avec input
    char = None
    # Je definie une variable tries pour savoir le nombre d'essaies réalisé
    #genere le caractère winCondition
    tries = 0
    #Tant que la variable char n'est pas égal au caractère winCondition
    while (char != winCondition):
        #Je redéfinis la variable char par un caractere genere au hasard avec input
        char = input()
        #J'incremente la variable tries
        tries = tries + 1
    #J'affiche la variable tries
    print(tries)

tablo =[0,15,3,0,5,7,9]
#Pour récupérer le 3
tablo[2]
#Pour la longeur du tableau
len(tablo)


prenom = "Benjamin"
nom = "Turcat"

nomPrenom = nom + prenom #Renvoie TurcatBenjamin
nomPrenom = nom + " " + prenom # Revoie Turcat Benjamin
intergerValue = 342
stringIntergerValue = str(342) #Renvoie "342" au lieu de 342

tableauMultiType= ["Benjamin", True, tablo, 4 > 2, None]
tableauDim = [0, 1, 2, 3]
tableauDim2 = [ 0, 5, 6, 3, 7]
tableauMultiDim = [tableauDim,tableauDim2]
tableauMultiDim[1][2]#Renvoi 6

tableauCleVal = {"Cle" : "Valeur"}
tableauCleVal["Cle"]#Renvoi "Valeur"



#Exo
#Faire une fonction qui concatene 2 chaines de caractere, les séparants par une virgule


#EXO 2:
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant un chaine de caractere
#avec l'enssemble des occuration d'un chiffre e.g :
#pour le tableau =[0,1,1,1,0,1,1,0,1]
#la fonction (tableau,0) doit renvoyer "0,4,7" n'hesitez pas a implementer la premiere fonction

#EXO 3:
#Tel que
listeUtilisateur = {
    "Benjamin" : "motdepasse",
    "Michel" : "password",
    "Toto" : "12345",
    "JoeMama" : "azerty",
}
#Ecrire une fonction login(userName,password,listUser) permettant d'afficher un message de connexion si
#le combo user/password est bon

