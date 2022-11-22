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
    for x in range(3):
        if tablo[x][0] == 'X' :
            if tablo[x][1] == 'X':
                return (x,'1')
            elif tablo[x][2] == 'X':
                return (x,'2')
        elif tablo[x][1] == 'X' :
            if tablo[x][2] == 'X':
                return (x,'3')
        #Verification veticale pour les X
        if tablo[0][x] == 'X':
            if tablo[1][x] == 'X':
                return ('4',x)
            elif tablo[2][x] == 'X' :
                return ('5',x)
        elif tablo[1][x] == 'X':
            if tablo[2][x] == 'X' :
                return ('6',x)
    #Verification de la premiere diagonale pour X
    if tablo[0][0] == 'X' :
        if tablo[1][1] == 'X':
            return '7'
        elif tablo[2][2] == 'X' :
            return '8'
    elif tablo[1][1] == 'X' :
        if tablo[2][2] == 'X' :
            return '9'
    #Verification de la deuxieme diagonale pour X
    if tablo[0][2] == 'X' :
        if tablo[1][1] == 'X':
            return '10'
        elif tablo[2][0] == 'X' :
            return '11'
    elif tablo[1][1] == 'X' :
        if tablo[2][0] == 'X' :
            return '12'
         

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
    
    while compteur < 9 :
        joue = False
        playerOne = input()
        if playerOne == '1' :
            if tab2[0] == '1':
                tab2[0] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '2' :
            if tab2[1] == '2':
                tab2[1] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '3' :
            if tab2[2] == '3':
                tab2[2] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '4' :
            if tab1[0] == '4':
                tab1[0] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '5' :
            if tab1[1] == '5':
                tab1[1] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '6' :
            if tab1[2] == '6':
                tab1[2] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '7' :
            if tab0[0] == '7':
                tab0[0] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '8' :
            if tab0[1] == '8':
                tab0[1] = 'X'
            else:
                print("emplacement deja utilisé")
        elif playerOne == '9' :
            if tab0[2] == '9':
                tab0[2] = 'X'
            else:
                print("emplacement deja utilisé")
        
        compteur = compteur + 1
        afficherMorpion(tableau)


        if verifAlign(tableau) == 'X' :
            print("Le player One a gagné")
            return
        elif verifAlign(tableau) == 'O':
            print("Le player Two a gagné")
            return
        elif compteur == 9 :
            print('égalité')
            return

        if verifAlignBis(tableau) == (0,'1'):
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (1,'1'):
            if tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (2,'1'):
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (0,'2'):
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (1,'2'):
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (2,'2'):
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (0,'3'):
            if tab0[0] == '7' :
                tab0[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (1,'3'):
            if tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == (2,'3'):
            if tab2[0] == '1' :
                tab2[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('4',0):
            if tab2[0] == '1' :
                tab2[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('4',1):
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('4',2):
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('5',0):
            if tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('5',1):
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('5',2):
            if tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('6',0):
            if tab0[0] == '7':
                tab0[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('6',1):
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == ('6',2):
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == '7':
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        elif verifAlignBis(tableau) == '8':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == '9':
            if tab0[0] == '7':
                tab0[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == '10':
            if tab2[0] == '1':
                tab2[0] = 'O'
                joue = True
        elif verifAlignBis(tableau) == '11':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignBis(tableau) == '12':
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        if joue == False :
            if tab1[1] == '5':
                tab1[1] = 'O'
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
        
        if verifAlign(tableau) == 'X' :
            print("Le player One a gagné")
            return
        elif verifAlign(tableau) == 'O':
            print("Le player Two a gagné")
            return
        compteur = compteur + 1
        print('---------------')
        afficherMorpion(tableau)   
        
        
morpion()
