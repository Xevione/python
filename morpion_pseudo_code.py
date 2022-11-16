#DEBUT

#Definir une fonction afficherMorpion() qui prend en compte un tableau de tableaux pour faire l'affichage du morpion
    #afficher le prmier tableau
    #afficher le deuxieme tableau
    #afficher le troisieme tableau

#Definir une fonction verifAlign() qui verifie si il y a trois 'X' ou 'O' sont alignés
    #Pour x de 0 a 2
        #Si les X sont aligné horizontalement
            #Renvoi Vrai,'X'
        #SinonSi les O sont aligné horizontalement
            #Renvoi Vrai,'O'
        #SinonSi les X sont aligné verticalement
            #Renvoi Vrai,'X'
        #SinonSi les O sont aligné verticalement
            #Renvoi Vrai,'O'
    #Si les X sont aligné en diagonales
        #Renvoi Vrai,'X'
    #SinonSi les O sont aligné en diagonales
        #Renvoi Vrai,'O'

#Definir un fonction morpion() qui simule une partie de morpion
    #initialisé tab0 qui a 3 caractère
    #initialisé tab1 qui a 3 caractère
    #initialisé tab2 qui a 3 caractère
    #initialisé tableau qui possède les 3 tableaux précédents
    #initialisation d'un compteur a 0
    #Tant que compteur inferieur a 9
        #on initialise playerOne en input pour que le premier joueur choisi où mettre son X
        #on verifie que l'emplacement est n'est pas deja pris:
            #on met un X a l'emplacement choisit
            #On affiche le morpion
        #On verifie si quelqu'un a gagné
            #Si oui
                #Renvoyer le gagnant
                #afficher le morpion
            #Sinon continuer
        #On initialise playerTwo en input pour que le deuxieme joueur choisi où mettre son O
        #On verifie que l'emplacement n'est pas deja pris
            #on met un O a l'emplacement choisit
            #On affiche le morpion
        #On verifie si quelqu'un a gagné
            #Si oui
                #Renvoyer le gagnant
                #afficher le morpion
            #Sinon continuer

#FIN