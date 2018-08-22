class Nasheed(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

allah_akbar = Nasheed(["allah akbar allah akbar allah akbar", "laa elah ela allah","allah akbar allah akbar","wa llah el-hamd"])
allah_akbar.sing_me_a_song()