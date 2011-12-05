import unittest

class Rubrique:

	global title,parent 

	def __init__(self,title, parent=None):
		self.title=title
		self.parent=parent

	def __str__(self):
		toReturn= "Rubrique '"+self.title+"'"
		if(self.parent==None):
			toReturn+=" racine "
		else:	
			toReturn+=" parent=("+self.parent.title+")'" 
		return toReturn

class RubriqueTest(unittest.TestCase):


	def test_init(self):
		r1 = Rubrique("Rubrique1")
		r2 = Rubrique("Rubrique2")
		r21 = Rubrique("Rubrique21", r1)

		print r1
		print r2
		print r21
		
		self.assertEqual("Rubrique21",r21.title)
		self.assertIsNotNone(r21.parent)

if __name__== '__main__':
	unittest.main()
