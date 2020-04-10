"""
Module card2.
Definit une classe Card et un petit cas-test qui demontre son utilite.
TODO: 
  - coder la fonction str
  - le init qui prend 0 ou 2 parametres (indication : chercher sur StackOverflow "python optional arguments in initializer of python class")
  - coder points ; d'ailleurs, est-ce une fonction ou un attribut ? 
  - corriger le bug : qui est que le 10 est plus fort que Dame Roi Valet (7 8 9 V D R 10 As) 
  - bonus : ajouter les atouts
  - bonus : ajouter un setter qui empeche couleur = "VERTE"
"""
from enum import Enum


Color = Enum("Color", "coeur carreau pique trefle")
	
class Valeur(Enum):
	SEPT = 7
	HUIT = 8
	NEUF = 9
	DIX = 10
	VALET = 11
	DAME = 12
	ROI = 13
	AS = 14

class Card:
	def __init__(self, valeur = None, couleur = None):
		self.couleur = couleur
		self.valeur = valeur
		self.points = 0


	def __str__(self):
		p = str(Color(self.couleur).name)  #FIXME
		q = str(Valeur(self.valeur).name)
		return (q + " de " + p)
        
	def points_carte (self):
		if (self.valeur == 7) or (self.valeur == 8) or (self.valeur == 9):
			self.points = 0
		if self.valeur == DIX :
			self.points = 10
		if self.valeur == VALET:
			self.points = 2
		if self.valeur == DAME :
			self.points = 3
		if self.valeur == ROI :
			self.points = 4
		if self.valeur ==  AS :
			self.points = 11
		
        
    

card1 = Card(ROI, PIQUE)
card1.points_carte()
# ~ card1 = Card()
# ~ card1.couleur = Color.COEUR
# ~ card1.valeur = 10

# card1.couleur = "VERTE"


card2 = Card(10, PIQUE)
card2.points_carte()
# ~ card2.valeur = 9
# card2.couleur = Color.COEUR

#
print("Le joueur 1 joue la carte", card1) 
print("Le joueur 2 joue la carte", card2)
print("qui a la meilleure carte ?")

## maintenant on compare des cartes
# atout ? 
if card1.couleur == card2.couleur:
	if card1.valeur != DIX and card2.valeur != DIX :
		if card1.valeur > card2.valeur :
			print("C'est J1 qui gagne avec", card1)
		else:
			print("C'est J2 qui gagne avec", card2)
	else :
		if card1.valeur == DIX :
			if card2.valeur == AS :
				print("C'est J2 qui gagne avec", card2)
			else : 
				print("C'est J1 qui gagne avec", card1)
		else : 
			if card1.valeur == AS :
				print("C'est J1 qui gagne avec", card1)
			else : 
				print("C'est J2 qui gagne avec", card2)
			
		
else:
	print("FIXME")
        

print("Et ça vaut ", card1.points + card2.points)

 
