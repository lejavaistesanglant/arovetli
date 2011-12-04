from Article import Article
import unittest

class ArticleTest(unittest.TestCase):

	global art

	def test_init(self):
		art = Article('first','Cedric')
		self.assertEqual('first',art.title)
		self.assertEqual('Cedric',art.author)

if __name__ == '__main__':
	unittest.main()
