import re
import reprlib
from collections import abc

RE_WORD=re.compile('\w+')

class Sentence:

	def __init__(self,text):
		self.text=text
		self.words=RE_WORD.findall(text)

	def __getitem__(self,index):
		return self.words[index]

	def __len__(self):
		return len(self.words)

	def __repr__(self):
		# components=reprlib.repr(self.text)
		# components=components[components.find('['):-1]
		# return 'Sentence({})'.format(components)
		return 'Sentence(%s)' % reprlib.repr(self.text)


s=Sentence('"The time has come," the Walrus said,')
# print(s)
for word in s:
	print(word)
print(list(s),len(s))
print(repr(s))
print(s[0],s[5],s[-1])
print(iter(s))
print(issubclass(Sentence,abc.Iterable))
print(isinstance(s,abc.Iterable))
s3=Sentence('Pig and pepper')