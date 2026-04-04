import fonct
cond=True
reponse=""
calcul1=fonct.Calculatrice(None,None,None)
while(cond):

    reponse=input("Entrez une opération (addition, soustraction, multiplication, division) ou 'quitter' pour terminer : ")
    if reponse == "quitter":
        break
    calcul1.nom = reponse
    calcul1.a = float(input("Entrez le premier nombre : "))
    calcul1.b = float(input("Entrez le deuxième nombre : "))
    calcul1.calcul()
    calcul1.historique()
    reponse=input("voulez vous voir l'historique des calculs ? (oui/non)")
    if reponse == "oui":
        
        print(calcul1.historique_calculs)
    else:
        cond=True
