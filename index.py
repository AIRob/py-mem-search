#coding:utf-8
#  建索引
from doc import Doc
import jieba

class Indexer:
	inverted = {}
	df = {}
	id_doc = {}

	def __init__(self,filepath):
		self.index_by_file(filepath)

	def index_by_file(self,filepath):
		doclist = []
		for line in open(filepath,'r').readlines():
			cols = line.rstrip().split('\t')
			if len(cols) == 3:
				id = cols[0]
				name = cols[1]
				text = cols[2]
				doc = Doc(id,name,text)
				doclist.append(doc)
		self.index(doclist)


	def index(self,doclist):
		for doc in doclist:

			#正排
			self.id_doc[doc.id] = doc


			#倒排
			term_list = jieba.cut_for_search(doc.text)
			for t in term_list:
				if t in self.inverted and doc.id not in self.inverted[t]:
					self.inverted[t].append(doc.id)
				else:
					self.inverted[t]=[doc.id]

		for t in self.inverted:
			self.df[t] = len(self.inverted)

		print "inverted terms:%d" % len(self.inverted)
		print "index done"

if __name__ == '__main__':
	print "index"
	print Indexer("docs.txt")
