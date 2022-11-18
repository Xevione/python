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

def morpion() : 
    #on initialise les tableaux du morpion
    tab0 = ['7','8','9']
    tab1 = ['4','5','6']
    tab2 = ['1','2','3']
    #on stock tout les tableaux dans un tableau
    tableau = [tab0,tab1,tab2]
    #on initialise un compteur a 0
    compteur = 0
    #on affiche le morpion
    afficherMorpion(tableau)
    #Tant que le compteur est inférieur a 9 ()
    while compteur < 9 :
        #on initialise playerOne en input du premier joueur
        playerOne = input()
        #Le PlayerOne choisit son emplacment
        if playerOne == '1' :
            #Si il est vide
            if tab2[0] == '1':
                #On met le X a l'emplacment choisit
                tab2[0] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '2' :
            #Si il est vide
            if tab2[1] == '2':
                #On met le X a l'emplacment choisit
                tab2[1] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '3' :
            #Si il est vide
            if tab2[2] == '3':
                #On met le X a l'emplacment choisit
                tab2[2] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '4' :
            #Si il est vide
            if tab1[0] == '4':
                #On met le X a l'emplacment choisit
                tab1[0] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '5' :
            #Si il est vide
            if tab1[1] == '5':
                #On met le X a l'emplacment choisit
                tab1[1] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '6' :
            #Si il est vide
            if tab1[2] == '6':
                #On met le X a l'emplacment choisit
                tab1[2] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '7' :
            #Si il est vide
            if tab0[0] == '7':
                #On met le X a l'emplacment choisit
                tab0[0] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '8' :
            #Si il est vide
            if tab0[1] == '8':
                #On met le X a l'emplacment choisit
                tab0[1] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")
        #Le PlayerOne choisit son emplacment
        elif playerOne == '9' :
            #Si il est vide
            if tab0[2] == '9':
                #On met le X a l'emplacment choisit
                tab0[2] = 'X'
                #afficher le morpion
                afficherMorpion(tableau)
                #On incremente le compteur
                compteur = compteur + 1
            #Sinon l'emplacement n'est pas libre
            else:
                #Donc afficher ce message
                print("emplacement deja utilisé")

        #Si verifAlign nous renvoi X
        if verifAlign(tableau) == 'X' :
            #Alors afficher que le PlayerOne a gagné
            print("Le player One a gagné")
            #arrete la partie
            return
        #Si verifAlign nous renvoi O
        elif verifAlign(tableau) == 'O':
            #Alors afficher que le PlayerTwo a gagné
            print("Le player Two a gagné")
            #arrete la partie
            return

        #meme commentaires pour le joueur deux
        playerTwo = input()
        if playerTwo == '1' :
            if tab2[0] == '1':
                tab2[0] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '2' :
            if tab2[1] == '2':
                tab2[1] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '3' :
            if tab2[2] == '3':
                tab2[2] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '4' :
            if tab1[0] == '4':
                tab1[0] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '5' :
            if tab1[1] == '5':
                tab1[1] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '6' :
            if tab1[2] == '6':
                tab1[2] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '7' :
            if tab0[0] == '7':
                tab0[0] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '8' :
            if tab0[1] == '8':
                tab0[1] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")
        elif playerTwo == '9' :
            if tab0[2] == '9':
                tab0[2] = 'O'
                afficherMorpion(tableau)
                compteur = compteur + 1
            else:
                print("emplacement deja utilisé")

        if verifAlign(tableau) =='X' :
            print("Le player One a gagné")
            return
        elif verifAlign(tableau) == 'O':
            print("Le player Two a gagné")
            return
morpion()