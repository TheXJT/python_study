import re
import reprlib
from collections import abc

RE_WORD=re.compile('\w+')

class Sentence:

	def __init__(self,text):
		self.text=text
		self.words=RE_WORD.findall(text)

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)

	def __iter__(self):
		for word in self.words:
			yield word
		return

s=Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
	print(word)
print(list(s))
print(issubclass(Sentence,abc.Iterable))
print(isinstance(s,abc.Iterable))