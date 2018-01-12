from bottle import route, run, template, view, get, post, request
from random import randint
@get('/hello/world')
def hello():
	numAlt = randint(1,100)
	num = " "
	return template('world_template',num=num, numAlt = numAlt)

@post('/hello/world')
def hola():
	num = request.forms.get('fname')
	numAlt = request.forms.get('numAlt')

	if numAlt == num:
		return template('world_template',num="Has Ganado!!! El numero es " + numAlt, numAlt = numAlt)
	elif numAlt < num:
		return template('world_template',num="El numero es menor", numAlt = numAlt)
	elif numAlt > num:
		return template('world_template',num="El numero es mayor", numAlt = numAlt)

run(host='localhost', port=8080)



