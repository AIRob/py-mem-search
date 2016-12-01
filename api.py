#coding:utf-8
from flask import Flask,jsonify,request,send_from_directory
from crossdomain import crossdomain

from index import Indexer
from search import Searcher

import urllib
import json

app = Flask(__name__, static_url_path='')

@app.route("/")
def main():
    return send_from_directory('static', 'search.html')


@app.route("/q/<input>")
@crossdomain(origin='*')
def search(input):
   	print urllib.unquote_plus(input).encode('utf-8')
	doclist = searcher.search(input)

	result = []
	for doc in doclist:
		result.append( str(doc.id)+", "+str(doc.name)+"<br>"+doc.text )

	return json.dumps(result)


index = Indexer("docs.txt")
searcher = Searcher(index)

if __name__ == "__main__":
	app.run(host='127.0.0.1',port=8282,debug=True)
