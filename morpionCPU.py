def afficherMorpion(tab):
    #Afficher le premier tableau
    print(tab[0])
    #Afficher le deuxieme tableau
    print(tab[1])
    #Afficher le troisieme tableau
    print(tab[2])

def verifAlign(tablo):
    #on fait une boucle pour verifier chaque ligne horizontale puis verticale
    for x in range(3):
        #Verification horizontale pour les X
        if tablo[x][0] == 'X' and tablo[x][1] == 'X' and tablo[x][2] == 'X' :
            #Renvoi X
            return 'X'
        #Verification horizontale pour les O
        elif tablo[x][0] == 'O' and tablo[x][1] == 'O' and tablo[x][2] == 'O' :
            #Renvoi O
            return 'O'
        #Verification veticale pour les X
        elif tablo[0][x] == 'X' and tablo[1][x] == 'X' and tablo[2][x] == 'X' :
            #Renvoi X
            return 'X'
        #Verification veticale pour les O
        elif tablo[0][x] == 'O' and tablo[1][x] == 'O' and tablo[2][x] == 'O' :
            #Renvoi O
            return 'O'
    #Verification de la premiere diagonale pour X
    if tablo[0][0] == 'X' and tablo[1][1] == 'X' and tablo[2][2] == 'X' :
         #Renvoi X
        return 'X'
    #Verification de la premiere diagonale pour O
    elif tablo[0][0] == 'O' and tablo[1][1] == 'O' and tablo[2][2] == 'O' :
        #Renvoi O
        return 'O'
    #Verification de la deuxieme diagonale pour X
    elif tablo[0][2] == 'X' and tablo[1][1] == 'X' and tablo[2][0] == 'X' :
         #Renvoi X
        return 'X'
    #Verification de la deuxieme diagonale pour O
    elif tablo[0][2] == 'O' and tablo[1][1] == 'O' and tablo[2][0] == 'O' :
        #Renvoi O
        return 'O'

    
def verifAlignBis(tablo):
    #on initialise le tableau
    tab = []
    #On fait une boucle de 0 a 2
    for x in range(3):
        #pour detecter un alignement de deux X horizontale
        if tablo[x][0] == 'X' :
            if tablo[x][1] == 'X':
                tab.append((x,'1'))
            elif tablo[x][2] == 'X':
                tab.append((x,'2'))
        elif tablo[x][1] == 'X' :
            if tablo[x][2] == 'X':
                tab.append((x,'3'))
        #pour detecter un alignement de deux X verticale
        if tablo[0][x] == 'X':
            if tablo[1][x] == 'X':
                tab.append(('4',x))
            elif tablo[2][x] == 'X' :
                tab.append(('5',x))
        elif tablo[1][x] == 'X':
            if tablo[2][x] == 'X' :
                tab.append(('6',x))
    #Verification de la premiere diagonale pour X
    if tablo[0][0] == 'X' :
        if tablo[1][1] == 'X':
            tab.append('7')
        elif tablo[2][2] == 'X' :
            tab.append('8')
    elif tablo[1][1] == 'X' :
        if tablo[2][2] == 'X' :
            tab.append('9')
    #Verification de la deuxieme diagonale pour X
    if tablo[0][2] == 'X' :
        if tablo[1][1] == 'X':
            tab.append('10')
        elif tablo[2][0] == 'X' :
            tab.append('11')
    elif tablo[1][1] == 'X' :
        if tablo[2][0] == 'X' :
            tab.append('12')
    return tab



def verifAlignWin(tablo):
    #pareil que verifAlignBis mais pour que le bot puisse gagné
    for x in range(3):
        if tablo[x][0] == 'O' :
            if tablo[x][1] == 'O':
                return (x,'13')
            elif tablo[x][2] == 'O':
                return (x,'14')
        elif tablo[x][1] == 'O' :
            if tablo[x][2] == 'O':
                return (x,'15')
        #Verification veticale pour les O
        if tablo[0][x] == 'O':
            if tablo[1][x] == 'O':
                return ('16',x)
            elif tablo[2][x] == 'O' :
                return ('17',x)
        elif tablo[1][x] == 'O':
            if tablo[2][x] == 'O' :
                return ('18',x)
    #Verification de la premiere diagonale pour O
    if tablo[0][0] == 'O' :
        if tablo[1][1] == 'O':
            return '19'
        elif tablo[2][2] == 'O' :
            return '20'
    elif tablo[1][1] == 'O' :
        if tablo[2][2] == 'O' :
            return '21'
    #Verification de la deuxieme diagonale pour O
    if tablo[0][2] == 'O' :
        if tablo[1][1] == 'O':
            return '22'
        elif tablo[2][0] == 'O' :
            return '23'
    elif tablo[1][1] == 'O' :
        if tablo[2][0] == 'O' :
            return '24'
         

def morpion() : 
    #on initialise les tableaux du morpion
    tab0 = ['7','8','9']
    tab1 = ['4','5','6']
    tab2 = ['1','2','3']
    #on stock tout les tableaux dans un tableau
    tableau = [tab0,tab1,tab2]
    #on initialise un compteur a 0
    compteur = 0
    #on initialise un index pour les contre
    contre = 0
    #on initailise un tableaContre pour 
    tableauContre = []
    #Tant que le compteur est inférieur a 9
    while compteur < 9 :
        #initialisation de joueContre
        joueContre = True
        #initialisation de joue a False
        joue = False
        #initialisation de playerOne en tant qu'input str
        playerOne = input()
        #EasterEGG
        if playerOne =='FFC':
            tabA = ['Fahima']
            tabB = ['Fried']
            tabC = ['Chicken']
            print(tabA)
            print(tabB)
            print(tabC)
            return
        #Si le player rentre '1
        elif playerOne == '1' :
            #Si la case est libre
            if tab2[0] == '1':
                #On met un X a l'emplacement demandé
                tab2[0] = 'X'
            #Sinon
            else:
                #renvoyer que l'emplacment est deja utilisé
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '2' :
            if tab2[1] == '2':
                tab2[1] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '3' :
            if tab2[2] == '3':
                tab2[2] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '4' :
            if tab1[0] == '4':
                tab1[0] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '5' :
            if tab1[1] == '5':
                tab1[1] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '6' :
            if tab1[2] == '6':
                tab1[2] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '7' :
            if tab0[0] == '7':
                tab0[0] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '8' :
            if tab0[1] == '8':
                tab0[1] = 'X'
            else:
                print("emplacement deja utilisé")
        #Idem
        elif playerOne == '9' :
            if tab0[2] == '9':
                tab0[2] = 'X'
            else:
                print("emplacement deja utilisé")
        
        #On incremente le compteur
        compteur = compteur + 1
        #On affiche le morpion
        afficherMorpion(tableau)

        #On verifie si le joueur 1 a gagné
        if verifAlign(tableau) == 'X' :
            #Afficher qu'il a gagné
            print("Le player One a gagné")
            #affiche le morpion
            afficherMorpion(tableau) 
            #on renvoi pour arreté
            return
        #Si le compteur est égal a 9
        elif compteur == 9 :
            #Affiche égalité
            print('égalité')
            #on renvoi pour arreté
            return
        #On met tout les messages de renvoi VerifAlignBis
        for i in range (len(verifAlignBis(tableau))):
            if verifAlignBis(tableau)[i] not in tableauContre:
                tableauContre.append(verifAlignBis(tableau)[i])

        
        #Si le bot peut gagné
        if verifAlignWin(tableau) == (0,'13'):
            #il verifie que l'emplacement est vide
            if tab0[2] == '9':
                #On met a l'emplacement pour gagné
                tab0[2] = 'O'
                #On passe la variable joue a True
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (1,'13'):
            if tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (2,'13'):
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (0,'14'):
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (1,'14'):
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (2,'14'):
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (0,'15'):
            if tab0[0] == '7' :
                tab0[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (1,'15'):
            if tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == (2,'15'):
            if tab2[0] == '1' :
                tab2[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('16',0):
            if tab2[0] == '1' :
                tab2[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('16',1):
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('16',2):
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('17',0):
            if tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('17',1):
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('17',2):
            if tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('18',0):
            if tab0[0] == '7':
                tab0[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('18',1):
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == ('18',2):
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == '19':
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == '20':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == '21':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == '22':
            if tab2[0] == '1':
                tab2[0] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == '23':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        #Idem
        elif verifAlignWin(tableau) == '24':
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        #Si le tableauContre n'est pas vide
        if tableauContre :
            #Si le contre est inférieur ou égale a la longueur du tableau moin 1
            if contre <= (len(tableauContre)) - 1:
                #Si joueContre est vrai
                while joueContre :
                    #Si contre est égale a la longeur de la tableContre
                    if contre == len(tableauContre):
                        #On passe joueContre a False
                        joueContre = False
                    #Sinon Si le tableau a l'indice de contre est égal a un message de verifAlignBis et que l'emplacement est libre Alors
                    elif tableauContre[contre] == (0,'1') and tab0[2] == '9':
                            #On met un O a l'emplacement pour bloqué
                            tab0[2] = 'O'
                            #On incrémente le contre
                            contre = contre + 1
                            #On passe joue a True
                            joue = True
                            #On passe joueContre a False
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (1,'1') and tab1[2] == '6':
                            tab1[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (2,'1') and tab2[2] == '3':
                            tab2[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (0,'2') and tab0[1] == '8':
                            tab0[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (1,'2') and tab1[1] == '5':
                            tab1[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (2,'2') and tab2[1] == '2':
                            tab2[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (0,'3') and tab0[0] == '7':
                            tab0[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (1,'3') and tab1[0] == '4':
                            tab1[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == (2,'3') and tab2[0] == '1':
                            tab2[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('4',0) and tab2[0] == '1':
                            tab2[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('4',1) and tab2[1] == '2':
                            tab2[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('4',2) and tab2[2] == '3':
                            tab2[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('5',0) and tab1[0] == '4':
                            tab1[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('5',1) and tab1[1] == '5':
                            tab1[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('5',2) and tab1[2] == '6':
                            tab1[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('6',0) and tab0[0] == '7':
                            tab0[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('6',1) and tab0[1] == '8':
                            tab0[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == ('6',2) and tab0[2] == '9':
                            tab0[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == '7' and tab2[2] == '3':
                            tab2[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == '8' and tab1[1] == '5':
                            tab1[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == '9' and tab0[0] == '7':
                            tab0[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == '10' and tab2[0] == '1':
                            tab2[0] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == '11' and tab1[1] == '5':
                            tab1[1] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Idem
                    elif tableauContre[contre] == '12' and tab0[2] == '9':
                            tab0[2] = 'O'
                            contre = contre + 1
                            joue = True
                            joueContre = False
                    #Sinon
                    else:
                        #On incrémente contre de 1
                        contre = contre + 1
        

        #Si le bot n'a pas encore 
        if joue == False :
            #Si le player un choisit cette emplacement
            if playerOne == '7':
                #Alors on bloque le coin opposé
                if tab2[2] == '3':
                    tab2[2] = 'O'
                #Si le jouer a le milieu
                elif tab1[1] == 'X':
                    #on bloque un coin a coté
                    if tab0[2] == '9':
                        tab0[2] = 'O'
                    #On bloque un coin a coté
                    elif tab2[0] == '1':
                        tab2[0] =='O'
                #Sinon on place a coté du joueur 1
                elif tab0[1] == '8':
                    tab0[1] = 'O'
                elif tab1[0] == '4':
                    tab1[0] = 'O'
            #Idem
            elif playerOne == '9':
                if tab2[0] == '1':
                    tab2[0]= 'O'
                elif tab1[1] == 'X':
                    if tab0[0] == '7':
                        tab0[0] = 'O'
                    elif tab2[2] == '3':
                        tab2[2] = 'O'
                elif tab0[1] == '8':
                    tab0[1] = 'O'
                elif tab1[2] == '6':
                    tab1[2] = 'O'
            #Idem
            elif playerOne == '1':
                if tab0[2] == '9':
                    tab0[2] = 'O'
                elif tab1[1] == 'X':
                    if tab0[0] == '7':
                        tab0[0] = 'O'
                    elif tab2[2] == '3':
                        tab2[2] = 'O'
                elif tab2[1] == '2':
                    tab2[1] = 'O'
                elif tab1[0] == '4':
                    tab1[0] = 'O'
            #Idem
            elif playerOne == '3':
                if tab0[0] ==  '7':
                    tab0[0] = 'O'
                elif tab1[1] == 'X':
                    if tab0[2] == '9':
                        tab0[2] = 'O'
                    elif tab2[0] == '1':
                        tab2[0] =='O'
                elif tab2[1] == '2':
                    tab2[1] = 'O'
                elif tab1[2] == '6':
                    tab1[2] = 'O'
            #Si le le joueur 1 prend un coté
            elif playerOne == '4':
                #on prend les coins
                if tab0[0] == '7':
                    tab0[0] = 'O'
                elif tab2[0] == '1':
                    tab2[0] = 'O'
            elif tab1[1] == '5':
                tab1[1] = 'O'
            #Idem
            elif playerOne == '8':
                if tab0[0] == '7':
                    tab0[0] = 'O'
                elif tab0[2] == '9':
                    tab0[2] = 'O'
            #Idem
            elif playerOne == '6':
                if tab2[2] == '3':
                    tab0[0] = 'O'
                elif tab0[2] == '9':
                    tab0[2] = 'O'
            #Idem
            elif playerOne == '2':
                if tab2[2] == '3':
                    tab2[2] = 'O'
                elif tab2[0] == '1':
                    tab2[0] = 'O'
            #Sinon on joue les coups du bot dans cette ordres
            elif tab0[2] == '9':
                tab0[2] = 'O'
            elif tab0[0] == '7':
                tab0[0] = 'O'
            elif tab2[2] == '3':
                tab2[2] = 'O'
            elif tab2[0] == '1':
                tab2[0] = 'O'
            elif tab0[1] == '8':
                tab0[1] = 'O'
            elif tab1[0] == '4':
                tab1[0] = 'O'
            elif tab1[2] == '6':
                tab1[2] = 'O'
            elif tab2[1] == '2':
                tab2[1] = 'O'
        #On Verifie si le bot a gagné
        if verifAlign(tableau) == 'O':
            print("Le player Two a gagné")
            afficherMorpion(tableau) 
            return
        #On incremente le compteur
        compteur = compteur + 1
        print('---------------')
        #On affiche le morpion
        afficherMorpion(tableau)  
        
        
morpion()