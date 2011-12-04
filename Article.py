from datetime import date

class Article:
	
	#def title, content, pubdate, author

	def __init__(self,title, author, pubdate=date.today()):
		self.title=title
		self.author=author
		self.pubdate=pubdate

	def __str__(self):
		return self.title+" written by "+self.author+ " published on "+ str(self.pubdate)


art = Article("Premier","Cedric")
print art
