#DEBUT

#On admet une fonction random() qui renvoi un chiffre entre 0 et 2 inclus
#On admet une fonction input() qui recupere un chiffre rentrer par un joueur lors de son execution
#Definir une fonction pierreFeuilleCiseau qui simule un round de pierre feuille ciseau et nous renvoyant le gagnant (0 = pierre, 1 = feuille, 2 = ciseau)
    #Afficher : "Bienvenu au pierre feuille ciseau, le jeu est très simple et choissisé soit pirre(0), feuille(1) ou ciseau(2). La pierre bat le ciseau, le ciseau bat la feuille 
    # et la feuille bat la pierre. "
    #On initialise un playerOne avec input() et afficher :"Veuillez choisir un chiffre entre 0 et 2 inclus"
    #On initialise un playerTwo avec random()
    #on verifie si le playerOne a choisit un chiffre entre 0 et 2 inclus
    #Si le playerOne a bien choisit son chiffre
        #Alors
        #Si playerTwo a choisit 0 (pierre)
            #Alors egalité
            #On execute la fonction pierreFeuilleCiseau() pour rejouer la partie
        #Sinon si playerTwo a choisit 1 (feuille)
            #Alors afficher le playerTwo a gagné
        #Sinon playerTwo a choisit 2 (ciseau)
            #Alors afficher le playerOne a gagné
        #Si playerOne a choisit 1 (feuille)
            #Si playerTwo a choisit 0 (pierre)
                #Alors afficher le playerOne a gagné
            #Sinon si playerTwo a choisit 1 (feuille)
                #Alors egalité
                #On execute la fonction pierreFeuilleCiseau() pour rejouer la partie
            #Sinon playerTwo a choisit 2 (ciseau)
                #Alors afficher le playerTwo a gagné
        #Si playerOne a choisit 2 (ciseau)
            #Si playerTwo a choisit 0 (pierre)
                #Alors afficher le playerTwo a gagné
            #Sinon si playerTwo a choisit 1 (feuille)
                #Alors afficher le playerOne a gagné
            #Sinon playerTwo a choisit 2 (ciseau)
                #Alors egalité
                #On execute la fonction pierreFeuilleCiseau() pour rejouer la partie
    #Sinon le playerOne rechoisit une chiffre en précisant qu'il faut un chiffre entre 0 et 2 inclus

    
#Executer la fonction pierreFeuilleCiseau() et gagné une partie comme un gros BG

#Definir une fonction matchPFC() qui simule un match de pierre feuille ciseau
#On initialise scorePlayerOne a 0 pour le score du premier joueur 1
#On initialise scorePlayerTwo a 0 pour le score du premier joueur 2
#Tant que scorePlayerOne est inférieur a 3 ou que scorePlayerTwo est inferieur a 3
    #Alors Jouer un round avec la fonction pierreFeuilleCiseau()
    #Si la fonction nous renvoie "le playerOne a gagné"
        #Alors incrementé de 1 scorePlayerOne
    #Sinon le playerTwo a gagné
        #Alors incrementé de 1 scorePlayerTwo
#Renvoyer le score du premier joueur puis du deuxieme joueur

#Executer la fonction matchFPC()

#FIN