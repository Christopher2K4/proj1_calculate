# Initialisation de l'historique au niveau du module pour la persistance
historique = []



star={}
star.


def calcul( nom,a,b):
   nom=str(nom).lower()
   nom.strip()
   history={}
   match nom:
        case "addition"|"+":
             return f"{a} + {b} = {a+b}"
            

        case "soustraction"|"-":
             return f"{a} - {b} = {a-b}"
        case "multiplication"|"x":
             return f"{a} * {b} = {a*b}"
        case "division"|"/":
             if b==0:
                return "impossible de diviser par 0"
             else:
                return f"{a} / {b} = {a/b}"
        case "puissance":
             return f"{a} ^ {b} = {a**b}"       
        case "modulo":
                if b==0:
                    return "impossible de faire un modulo par 0"
                else:
                    return f"{a} % {b} = {a%b}"

historique=[]
    
def get_history(calcul):
    
     historique.append





   


   

  

          


    
