from bottle import route, run, template, view, get, post, request
from random import randint
@get('/hello/world')

def hello():
	numAlt = randint(1,100)
	num = None
	return template('world_template',num=num, numAlt = numAlt)

@post('/hello/world')

def hola():
	num = request.forms.get('fname')
	numAlt = request.forms.get('numAlt')

	if numAlt == num:
		return template('<h1>Hola</h1>')
run(host='localhost', port=8080)



