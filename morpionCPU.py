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
    tab = []
    for x in range(3):
        if tablo[x][0] == 'X' :
            if tablo[x][1] == 'X':
                tab.append((x,'1'))
            elif tablo[x][2] == 'X':
                tab.append((x,'2'))
        elif tablo[x][1] == 'X' :
            if tablo[x][2] == 'X':
                tab.append((x,'3'))
        #Verification veticale pour les X
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
    contre = 0
    tableauContre = []
    
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
            afficherMorpion(tableau) 
            return
        elif compteur == 9 :
            print('égalité')
            return

        for i in range (len(verifAlignBis(tableau))):
            if verifAlignBis(tableau)[i] not in tableauContre:
                tableauContre.append(verifAlignBis(tableau)[i])

        print(tableauContre)
        print(contre)
        
        
        if verifAlignWin(tableau) == (0,'13'):
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (1,'13'):
            if tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (2,'13'):
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (0,'14'):
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (1,'14'):
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (2,'14'):
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (0,'15'):
            if tab0[0] == '1' :
                tab0[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (1,'15'):
            if tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == (2,'15'):
            if tab2[0] == '1' :
                tab2[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('16',0):
            if tab2[0] == '1' :
                tab2[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('16',1):
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('16',2):
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('17',0):
            if tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('17',1):
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('17',2):
            if tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('18',0):
            if tab0[0] == '7':
                tab0[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('18',1):
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == ('18',2):
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == '19':
            if tab2[2] == '3':
                tab2[2] = 'O'
                joue = True
        elif verifAlignWin(tableau) == '20':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == '21':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == '22':
            if tab2[0] == '1':
                tab2[0] = 'O'
                joue = True
        elif verifAlignWin(tableau) == '23':
            if tab1[1] == '5':
                tab1[1] = 'O'
                joue = True
        elif verifAlignWin(tableau) == '24':
            if tab0[2] == '9':
                tab0[2] = 'O'
                joue = True

        if tableauContre :
            if contre <= len(tableauContre) - 1:
                print(tableauContre[contre])
                if tableauContre[contre] == (0,'1') and tab0[2] == '9':
                        tab0[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (1,'1') and tab1[2] == '6':
                        tab1[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (2,'1') and tab2[2] == '3':
                        tab2[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (0,'2') and tab0[1] == '8':
                        tab0[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (1,'2') and tab1[1] == '5':
                        tab1[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (2,'2') and tab2[1] == '2':
                        tab2[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (0,'3') and tab0[0] == '7':
                        tab0[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (1,'3') and tab1[0] == '4':
                        tab1[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == (2,'3') and tab2[0] == '1':
                        tab2[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('4',0) and tab2[0] == '1':
                        tab2[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('4',1) and tab2[1] == '2':
                        tab2[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('4',2) and tab2[2] == '3':
                        tab2[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('5',0) and tab1[0] == '4':
                        tab1[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('5',1) and tab1[1] == '5':
                        tab1[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('5',2) and tab1[2] == '6':
                        tab1[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('6',0) and tab0[0] == '7':
                        tab0[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('6',1) and tab0[1] == '8':
                        tab0[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == ('6',2) and tab0[2] == '9':
                        tab0[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == '7' and tab2[2] == '3':
                        tab2[2] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == '8' and tab1[1] == '5':
                        tab1[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == '9' and tab0[0] == '7':
                        tab0[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == '10' and tab2[0] == '1':
                        tab2[0] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == '11' and tab1[1] == '5':
                        tab1[1] = 'O'
                        contre = contre + 1
                        joue = True
                elif tableauContre[contre] == '12' and tab0[2] == '9':
                        tab0[2] = 'O'
                        contre = contre + 1
                        joue = True
                else:
                    contre = contre + 1
        elif playerOne == '7':
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
            elif tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        elif playerOne == '9':
            if tab0[1] == '8':
                tab0[1] = 'O'
                joue = True
            elif tab1[2] == '6':
                tab1[2] = 'O'
                joue = True
        elif playerOne == '1':
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
            elif tab1[0] == '4':
                tab1[0] = 'O'
                joue = True
        elif playerOne == '3':
            if tab2[1] == '2':
                tab2[1] = 'O'
                joue = True
            elif tab1[2] == '6':
                tab1[2] = 'O'
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
        
        if verifAlign(tableau) == 'O':
            print("Le player Two a gagné")
            afficherMorpion(tableau) 
            return
        compteur = compteur + 1
        print('---------------')
        afficherMorpion(tableau)  
        print(tableauContre)
        print(contre)
        
        
morpion()