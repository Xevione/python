from random import randint;
#Definir une fonction pierreFeuilleCiseau qui simule un round de pierre feuille ciseau et nous renvoyant le gagnant (0 = pierre, 1 = feuille, 2 = ciseau)
def pierreFeuilleCiseau():
    #Afficher : "Bienvenu au pierre feuille ciseau, le jeu est très simple et choissisé soit pirre(0), feuille(1) ou ciseau(2). La pierre bat le ciseau, le ciseau bat la feuille 
    # et la feuille bat la pierre. "
    print("Bienvenu au pierre feuille ciseau, le jeu est très simple et choissisé soit pirre(0), feuille(1) ou ciseau(2). La pierre bat le ciseau, le ciseau bat la feuille et la feuille bat la pierre.")
    #On initialise un playerOne avec input() et afficher :"Veuillez choisir un chiffre entre 0 et 2 inclus"
    playerOne = int(input())
    #On initialise un playerTwo avec random()
    playerTwo = randint(0,2)
    #Si le playerOne est entre 0 et 2 inclus
    if  playerOne < 3  and playerOne > -1 :
        #Si playerOne a choisit 0 (pierre)
        if playerOne == 0 :
            #Alors
            #Si playerTwo a choisit 0 (pierre)
            if playerTwo == 0 :
                #Alors egalité
                print("égalité")
                #On execute la fonction pierreFeuilleCiseau() pour rejouer la partie
                pierreFeuilleCiseau()
            #Sinon si playerTwo a choisit 1 (feuille)
            elif playerTwo == 1 :
                #Alors afficher le playerTwo a gagné
                print("le playerTwo a gagné")
                return "le playerTwo a gagné"
            #Sinon playerTwo a choisit 2 (ciseau)
            else :
                #Alors afficher le playerOne a gagné
                print("le playerOne a gagné")
                return "le playerOne a gagné"
        #Si playerOne a choisit 1 (feuille)
        if playerOne == 1 :
            #Si playerTwo a choisit 0 (pierre)
            if playerTwo == 0 :
                #Alors afficher le playerOne a gagné
                print("le playerOne a gagné")
                return "le playerOne a gagné"
            #Sinon si playerTwo a choisit 1 (feuille)
            elif playerTwo == 1 :
                #Alors egalité
                print("égalité")
                #On execute la fonction pierreFeuilleCiseau() pour rejouer la partie
                pierreFeuilleCiseau()
            #Sinon playerTwo a choisit 2 (ciseau)
            else :
                #Alors afficher le playerTwo a gagné
                print("le playerTwo a gagné")
                return "le playerTwo a gagné"
        #Si playerOne a choisit 2 (ciseau)
        if playerOne == 2 :
            #Si playerTwo a choisit 0 (pierre)
            if playerTwo == 0 :
                #Alors afficher le playerTwo a gagné
                print("le playerTwo a gagné")
                return "le playerTwo a gagné"
            #Sinon si playerTwo a choisit 1 (feuille)
            elif playerTwo == 1 :
                #Alors afficher le playerOne a gagné
                print("le playerOne a gagné")
                return "le playerOne a gagné"
            #Sinon playerTwo a choisit 2 (ciseau)
            elif playerTwo == 2 :
                #Alors egalité
                print("égalité")
                #On execute la fonction pierreFeuilleCiseau() pour rejouer la partie
                pierreFeuilleCiseau()
    #Sinon le playerOne rechoisit une chiffre en précisant qu'il faut un chiffre entre 0 et 2 inclus
    else :
        print("Veuillez choisir un chiffre entre 0 et 2 (0 et 2 inclus)")
        pierreFeuilleCiseau()


    
#Executer la fonction pierreFeuilleCiseau() et gagné une partie comme un gros BG

#Definir une fonction matchPFC() qui simule un match de pierre feuille ciseau
def matchPFC():
    #On initialise scorePlayerOne a 0 pour le score du premier joueur 1
    scorePlayerOne = 0
    #On initialise scorePlayerTwo a 0 pour le score du premier joueur 2
    scorePlayerTwo = 0
    #Tant que scorePlayerOne est inférieur a 3 ou que scorePlayerTwo est inferieur a 3
    while scorePlayerOne < 3 and scorePlayerTwo < 3 :
        #Alors Jouer un round avec la fonction pierreFeuilleCiseau()
        tmp = pierreFeuilleCiseau()
        #Si la fonction nous renvoie "le playerOne a gagné"
        if tmp == ("le playerOne a gagné") :
            #Alors incrementé de 1 scorePlayerOne
            scorePlayerOne = scorePlayerOne + 1
        #Sinon le playerTwo a gagné
        elif tmp == ("le playerTwo a gagné") :
            #Alors incrementé de 1 scorePlayerTwo
            scorePlayerTwo = scorePlayerTwo + 1
        else :
            scorePlayerOne = scorePlayerOne
            scorePlayerTwo = scorePlayerTwo
    #Renvoyer le score du premier joueur puis du deuxieme joueur
    print("scorePlayerOne : ",scorePlayerOne ,"scorePlayerTwo : ", scorePlayerTwo)
    return

matchPFC()
