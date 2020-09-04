from sympy import *
from math import *
x = symbols('x')
var = dict()


def calculate(text):
	# Calcula o que o usuário mandou.
	try:
		# Desafio pro Derick.
		if 'import' in text:
			raise SystemError
		else:
			if '^' in text:
				text = text.replace('^', '**')
			return eval(text)
	except ZeroDivisionError:
		return 'VAI DIVIDIR POR ZERO NÃO, SEU ARROMBADO!'
	except SystemError:
		return 'VAI INVADIR MEU PC NÃO, SEU ARROMBADO!'
	except:
		return 'Refaz a conta aí, meu chapa, tem alguma coisa errada.'


def make_var(text):
	global var
	try:
		if "^" in text:
			text = text.replace('^', '**')
		if 'poli' in text:
			raise AttributeError
		if 'clear' in text:
			var.clear()
			return 'Variables cleared'
		if 'show' in text:
			return f'var = {var}'
		if 'import' in text:
			raise SystemError
		if 'lambda' in text:
			var[text.split(' ')[0]] = eval(' '.join(text.split(' ')[2::]))
		else:
			var[text.split(' ')[0]] = float(text.split(' ')[2])
		return f'var = {var}'
	except AttributeError:
		return 'Easter egg encontrado!\nPoli não pode ser calculado, ele quem calcula você.'
	except SystemError:
		return 'VAI INVADIR MEU PC NÃO, SEU ARROMBADO!'
