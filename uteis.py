from time import sleep
from os import system, name
def line(tlin='-', tama=60):
	""" 
	Função que desenha uma linha na tela
	
	parametro tlin: tipo da linha
	parametro tama: tamanho da linha	
	"""
	tam = len(tlin)
	print(tlin * (tama//tam))


def end():
	"""
	Função de mantém programa aberto.
	
	sem parametros
	sem retorno
	"""
	input('\n\n\n\033[1;32mPrograma finalizado com sucesso. Aperte ENTER para sair.')


def title(msg, tl='-'):
	tam = len(msg) + 4
	print(tl * tam)
	print(f'  {msg}')
	print(tl * tam)


def inint(msg):
	ok = False
	val = 0
	while True:
		n = str(input(msg))
		if n.isnumeric():
			val = int(n)
			ok = True
		else:
			print('\033[31mERRO: Digite um número inteiro válido.\033[m')
		if ok:
			break
	return val


def erro():
	title('\033[31mERRO: Opção invalida.\033[m')
	sleep(2)


def fact(num=0,show=False):
	"""
	Função que retorna o fatorial de um número
	
	parametro num: Número a ser fatorado
	parametro show: Mostra ou não o calculo do fatorial
	retorno: O resultado do fatorial
	"""
	f = 1
	for c in range(num, 0, -1):
		if show == True:
			print(c, end='')
			if c > 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
		f *= c
	return f


def med(n1, n2, n3):
	media=(n1+n2+n2)/3
	print(media)


def clear():
	system('cls' if name == 'nt' else 'clear')

