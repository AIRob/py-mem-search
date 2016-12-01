#coding:utf-8
from index import Indexer
from search import Searcher


if __name__ == '__main__':
	index = Indexer("docs.txt")
	searcher = Searcher(index)

	i=0
	while 1:
		i+=1

		input = raw_input(str(i)+".请输入问题：")
		doclist = searcher.search(input.decode('utf-8'))

		if len(doclist) > 0:
			for doc in doclist:
				print doc.id,doc.name,doc.text
		else:
			print "无相关结果"
		print "\n"
