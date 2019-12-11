from flask import Flask, render_template, url_for, request
from flask_paginate import Pagination, get_page_args
import whoosh
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
from whoosh import qparser

app = Flask(__name__)
app.templates_folder = 'templates'


@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])

@app.route('/results/', methods=['GET', 'POST'])
def results():
	# global whooshSearcher
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args

	query = data.get('searchterm')
	# customRank = data.get('searchtype')
	# if customRank:
	# 	results = customSearcher.search(query)
	# else:
	# 	results = whooshSearcher.search(query)

	page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')

	ids = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14)
	names = ("Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft", "Craft")


	total = len(ids)

	pagination_results = zip(ids[offset: offset + per_page], names[offset: offset + per_page])

	pagination = Pagination(page=page, per_page=per_page, total=total, css_framework="semantic2")
 
	return render_template('search.html', query=query, results=pagination_results, per_page=per_page, pagination=pagination)

@app.route('/craft/', methods=['GET', 'POST'])
def craft():
	print(request.args)
	data = request.args
	craftid = data.get('craft')
	return ()

class MyWhooshSearcher(object):
	"""docstring for MyWhooshSearcher"""
	def __init__(self):
		super(MyWhooshSearcher, self).__init__()
		
		
	def search(self, queryEntered):
		title = list()
		description = list()
		with self.indexer.searcher() as search:
			query = MultifieldParser(['title', 'materials'], schema=self.indexer.schema)
			query = query.parse(queryEntered)
			results = search.search(query, limit=None)
			
			for x in results:
				title.append(x['title'])
				description.append(x['materials'])
			
		return title, materials

	def index(self):
		schema = Schema(id=ID(stored=True), title=TEXT(stored=True), description=TEXT(stored=True))
		indexer = create_in('myIndex', schema)
		writer = indexer.writer()

		writer.add_document(id=u'1', title=u'hello there', description=u'cs hello, how are you')
		writer.add_document(id=u'2', title=u'hello bye', description=u'nice to meetcha')
		writer.commit()

		self.indexer = indexer

if __name__ == '__main__':
	# global whooshSearcher
	# whooshSearcher = MyWhooshSearcher()
	# whooshSearcher.index()
	app.run(debug=True)
