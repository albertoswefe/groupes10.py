#fait par Albert Wefe 18A179FS
from Agent import Agent
 
class Guichetier(Agent): #Sous-Classe Guichetier ayant comme classe mere Personne
 
    # Notre méthode constructeur
    
    def __init__(self,mat = " ",nom = " ", prenom =" "):
     
        #Constructeur de notre classe
        # On appelle explicitement le constructeur de Agent :
        Agent.__init__(self,mat,nom,prenom)
 
    def affSolde(self,compte):
        print("\tGuichetier\nVotre solde disponible est de {0} FCFA ".format(compte.solde))
 
    def versement(self,compte = Compte(),mt = 0.0):
        # Un montant va etre ajouter au compte du client
        compte.versement(mt)
    
    def retrait(self,compte,mt):
        """ ici, un test va etre effectuer dans la classe Controlleur pour savoir si le solde disponible est suffisant """
        # Si "OUI" ... un retrait est effectuer par le Guichetier avec la permission du Controleur
        compte.retrait(mt)
        
    def preter(self,sommeDonner = 0.0,mt = 0.0):
        sommeDonner += mt
        print("\tGuichetier\nEmprunt de {0} FCFA éffectué ! ".format(mt))
    
    def __str__(self):
        return "\tGuichetier\n" + Agent.__str__(self)
