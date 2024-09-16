#### Fonction secondaire
"""
author : allan.carvalho@edu.esiee.fr
"""

def ispalindrome(p):
    """"
    prend en argument une chaîne de caractère et regarde si
    ce dernier est un palindrome 
    """
    if p[::-1] == p :
        return True
    return False

#### Fonction principale

def main():
    """
    Teste quelques mots pour voir si 
    la fonction marche
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
