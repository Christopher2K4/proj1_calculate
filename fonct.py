

class Calculatrice:
    historique_calculs = {}
#dictionnaire de donnees visant à stocker les calculs effectués
    def __init__(self, nom, a, b):
        self.nom = nom
        self.a = a
        self.b = b
        self.resultat = None
        self.compteur=0

    def calcul(self):
        self.compteur += 1
        if self.nom == "addition":
            self.resultat = self.a + self.b

        elif self.nom == "soustraction":
            self.resultat = self.a - self.b

        elif self.nom == "multiplication":
            self.resultat = self.a * self.b

        elif self.nom == "division":
            try:
                self.resultat = self.a / self.b
            except ZeroDivisionError:
                self.resultat = "Erreur : Division par zéro"

        else:
            self.resultat = "Opération non reconnue"

       
#focntion qui integre les resulatats dans le dico
    def historique (self):
        
        self.historique_calculs.update({self.compteur:self.resultat})
        return self.historique_calculs


# ─── Test ───────────────────────────────────────





