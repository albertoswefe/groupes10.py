

class Banque:
    def __init__(self,nom):
        self.nom=nom
       
class Guichitier(Banque):
  def __init__(self,nom, so=0, mon=12):
      Banque.__init__(self,nom)
      self.solde=so
      self.montant=mon
  def consultesolde (self):
      return self.soldesolde
  def retire (self,montant):
    if self.solde ˂= self.montant:
          print ("impossible de ce faire retraire")
      else:
        self.solde-=self.montant
      return self.solde
  def versement (self, montant):
                self.solde+=montant
     return self.solde
  def virement (self,comptc):
    self.retire(self,montant)
    comptc.versement(self,montant)
  def operation(self):
      self.versement(self,montant)
      self.retire(self,montant)
 # Auto-test ---------------------------------------------------------
if __name__ == '__main__':
r = Guichitier("nom",7845,122)
    print(r.retire(self,montant))
    print(r.consultesolde(self))
    print(r.versement(self,montant))
    print(r.virement(self,montant))
