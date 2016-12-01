#coding:utf-8
from index import Indexer
import jieba

import operator


# 搜索
# 返回结果：(相关问题,相似度)列表
# 搜索步骤：
#   1.分词
# 	2.找出候选doc
#	3.计算相似度
#	4.返回前10

class Searcher:

	def __init__(self,index):
		self.index = index;

	def search(self,query):
		answer_list=[]
		answer = []

		#分词
		term_list = jieba.cut_for_search(query)

		#计算tf
		tf = {}
		for term in term_list:
			if term in tf :
				tf[term] += 1
			else:
				tf[term] = 1

		#候选doc
		candidate_doc_id={}
		for term in tf:
			if term in self.index.inverted:
				term_weight = tf[term]*1.0/(1+self.index.df[term])
				for doc_id in self.index.inverted[term]:
					if doc_id in candidate_doc_id:
						candidate_doc_id[doc_id] += term_weight
					else:
						candidate_doc_id[doc_id] = term_weight

		#rank by length
		for doc_id in candidate_doc_id:
			candidate_doc_id[doc_id] /= len(self.index.id_doc[doc_id].text)


		sorted_doc = sorted(candidate_doc_id.items(), key=operator.itemgetter(1),reverse=True)

		res = []
		for (doc_id,weight) in sorted_doc[0:10]:
			res.append(self.index.id_doc[doc_id])
		return res


if __name__ == '__main__':
	index = Indexer("docs.txt")
	searcher = Searcher(index)
	doclist = searcher.search("中央调查")
	for doc in doclist:
		print doc.id,doc.name,doc.text

