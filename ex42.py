##This is example 40 from the 2nd edition of LPTHW

class song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = song(["Happy birthday to you",
		   "I do not want to get sued",
		   "So i will stop right here"])
		   
bulls_on_parade = song(["They rally around the family",
			"With pockets full of shells"])
			
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
