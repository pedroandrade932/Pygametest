from random import randint
from time import sleep
import uteis
from uteis import erro, inint
import pycolor
import sprites
dados = []
init1 = []
init2 = []
init3 = []
#-----------------------------------------
def viw(op):
	global dados, nev, fim, jlifesmax, jlifes, totex, ni, maxex, arefl, lamp, dmin, dmax, luz, sod, stage1, stage2, stage3, mapa
	global money, pocao, nome
	if op == 1:
		arquivo = open('save1.txt', 'r')
	elif op == 2:
		arquivo = open('save2.txt', 'r')
	elif op == 3:
		arquivo = open('save3.txt', 'r')
	for linha in arquivo:
		linha = linha.rstrip()
		if op == 1:
			init1.append(linha)
		if op == 2:
			init2.append(linha)
		if op == 3:
			init3.append(linha)
	arquivo.close()


def save(op):
	if op == 1:
		arquivo = open('save1.txt', 'w')
	elif op == 2:
		arquivo = open('save2.txt', 'w')
	elif op == 3:
		arquivo = open('save3.txt', 'w')
	arquivo.write(f'{nome}' + '\n')
	arquivo.write(f'{nev}' + '\n')
	arquivo.write(f'{fim}' + '\n')
	arquivo.write(f'{jlifesmax}' + '\n')
	arquivo.write(f'{jlifes}' + '\n')
	arquivo.write(f'{totex}' + '\n')
	arquivo.write(f'{ni}' + '\n')
	arquivo.write(f'{maxex}' + '\n')
	arquivo.write(f'{arefl}' + '\n')
	arquivo.write(f'{lamp}' + '\n')
	arquivo.write(f'{dmin}' + '\n')
	arquivo.write(f'{dmax}' + '\n')
	arquivo.write(f'{luz}' + '\n')
	arquivo.write(f'{sod}' + '\n')
	arquivo.write(f'{stage1}' + '\n')
	arquivo.write(f'{stage2}' + '\n')
	arquivo.write(f'{stage3}' + '\n')
	arquivo.write(f'{mapa}' + '\n')
	arquivo.write(f'{money}' + '\n')
	arquivo.write(f'{pocao}' + '\n')
	arquivo.write(f'{esp}' + '\n')
	arquivo.write(f'{elf}' + '\n')
	arquivo.write(f'{city}' + '\n')
	arquivo.write(f'{rpas}' + '\n')
	arquivo.write(f'{resp}' + '\n')
	arquivo.write(f'{zan}' + '\n')
	arquivo.write(f'{stage4}' + '\n')
	arquivo.write(f'{ctot}' + '\n')
	arquivo.close()


def change(op):
	global dados, nev, fim, jlifesmax, jlifes, totex, ni, maxex, arefl, lamp, dmin, dmax, luz, sod, stage1, stage2, stage3, mapa
	global money, pocao, nome, esp, elf, city, rpas, resp, zan, stage4
	if op == 1:
		arquivo = open('save1.txt', 'r')
	elif op == 2:
		arquivo = open('save2.txt', 'r')
	elif op == 3:
		arquivo = open('save3.txt', 'r')
	for linha in arquivo:
		linha = linha.rstrip()
		dados.append(linha)
	arquivo.close()
	if dados[0] != '':
		nome = dados[0]
		nev = dados[1]
		fim = dados[2]
		jlifesmax = int(dados[3])
		jlifes = int(dados[4])
		totex = int(dados[5])
		ni = int(dados[6])
		maxex = int(dados[7])
		arefl = dados[8]
		lamp = dados[9]
		dmin = int(dados[10])
		dmax = int(dados[11])
		luz = dados[12]
		sod = dados[13]
		stage1 = dados[14]
		stage2 = dados[15]
		stage3 = dados[16]
		mapa = dados[17]
		money = int(dados[18])
		pocao = int(dados[19])
		esp = dados[20]
		elf = dados[21]
		city = dados[22]
		rpas = dados[23]
		resp = dados[24]
		zan = dados[25]
		stage4 = dados[26]
		ctot = dados[27]
#-----------------------------------------


def lvup():
	global totex, maxex, ni, jlifesmax
	if totex >= maxex:
		ni += 1
		title(f'\033[32mVocê subiu para o nivel {ni}!!!\033[m')
		sleep(2)
		jlifesmax += 2
		title(f'\033[32mSua energia aumentou em 2!\033[m')
		totex -= 12
		sleep(2)



def title(msg, tl='-'):
	tam = len(msg) - 4
	print(tl * tam)
	print(f'  {msg}', flush='True')
	print(tl * tam)


def stitle(msg, tl='-'):
	tam = len(msg) + 4
	print(tl * tam)
	print(f'  {msg}')
	print(tl * tam)


def menuj():
	global nev, stage2, stage3, stage4, pocao, jlifes, jlifesmax, city
	while True:
		uteis.clear()
		title('>>> \033[33mMENU\033[m <<<')
		cit = ''
		if stage2 == 'True':
			cit = 'Kanaghin'
		elif stage3 == 'True':
			cit = 'Nevada'
		elif stage4 == 'True':
			cit = 'Mililand'
		porc = (jlifesmax * 42) // 100
		print('-='*16)
		if jlifes <= porc:
			print(f'Nome: {pycolor.green()}{nome:<14}{pycolor.nill()}Money: {pycolor.yellow(1)}{money}{pycolor.nill()}')
			print(f'Cidade: {cit:<12}Vida: {pycolor.red(5)}{jlifes}{pycolor.nill()}/{jlifesmax}')
		else:
			print(f'Nome: {pycolor.green()}{nome:<14}{pycolor.nill()}Money: {pycolor.yellow(1)}{money}{pycolor.nill()}')
			print(f'Cidade: {cit:<12}Vida: {pycolor.green()}{jlifes}{pycolor.nill()}/{jlifesmax}')
		print('-'*32)
		print(f'{"No.":<4}{"ITEM":<10}{"QUANT":>16}')
		print('-'*32)
		if mapa == 'True':
			print(f'{"1":<4}{"MAPA":.<10}{"inf":.>16}')
		if lamp == 'True':
			print(f'{"2":<4}{"LAMPIÃO":.<10}{"inf":.>16}')
		if pocao > 0:
			print(f'{"3":<4}{"POÇÃO":.<10}{pocao:.>16}')
		if mapa == 'False':
			print(f'{pycolor.white(3)}{"SEM ITENS NO MENU":^30}{pycolor.nill()}')
		print('-'*32)
		res = uteis.inint('Sua escolha: ')
		if res == 999:
			uteis.clear()
			break
		elif res == 1 and mapa == 'True':
			title('>>>\033[33mEsse é o mapa mundi, escolha a cidade.\033[m<<<')
			sleep(2)
			print('[ 1 ] Vila Kanaghin')
			if nev == 'True':
				print('[ 2 ] Nevada')
			if zan == 'True':
				print('[ 3 ] Mililand')
			res = uteis.inint('Sua escolha: ')
			if res == 1:
				title('\033[34mviajando...\033[m')
				sleep(2)
				title('\033[32mViagem realizanda com sucesso\033[m')
				sleep(2)
				stage2 = 'True'
				stage3 = 'False'
				stage4 = 'False'
			elif res == 2 and nev == 'True':
				title('\033[34mviajando...\033[m')
				sleep(2)
				title('\033[32mViagem realizanda com sucesso\033[m')
				sleep(2)
				stage2 = 'False'
				stage3 = 'True'
				stage4 = 'False'
			elif res == 3 and zan == 'True':
				title('\033[34mviajando...\033[m')
				sleep(2)
				title('\033[32mViagem realizanda com sucesso\033[m')
				sleep(2)
				stage2 = 'False'
				stage3 = 'False'
				stage4 = 'True'
			else:
				title('\033[31mERRO, essa cidade não existe... Será?\033[m')
		elif res == 2 and lamp == 'True':
			title('\033[32mAs luzes se acenderam.\033[m')
			sleep(2)
			luz = 'True'
		elif res == 3 and pocao > 0:
			if jlifes < jlifesmax:
				title('\033[32mVocê recuperou 10 de vida!\033[m')
				sleep(2)
				cal = (jlifes + 10) - jlifesmax
				if cal >=0:
					jlifes += 10 - cal
				else:
					jlifes += 10
				pocao -= 1
			else:
				title('\033[31mSua energia já está recuperada.\033[m')
				sleep(2)


def tsave():
	global init1, init2, init3
	viw(1)
	viw(2)
	viw(3)
	print('Salvar em qual arquivo?')
	sleep(2)
	print('-'*30)
	if init1 == []:
		print(f'[ 1 ] {pycolor.white(3)}Arquivo vazio.{pycolor.nill()}')
	else:
		if int(init1[4]) <= porc:
			print(f'[ 1 ] Nome: {pycolor.green()}{init1[0]}{pycolor.nill()}  Vidas: {pycolor.red(5)}{init1[4]}{pycolor.nill()}/{init1[3]}  Cidade: {init1[22]}')
		else:
			print(f'[ 1 ] Nome: {pycolor.green()}{init1[0]}{pycolor.nill()}  Vidas: {pycolor.green()}{init1[4]}{pycolor.nill()}/{init1[3]}  Cidade: {init1[22]}')
	if init2 == []:
		print(f'[ 2 ] {pycolor.white(3)}Arquivo vazio.{pycolor.nill()}')
	elif init2 != []:
		if int(init2[4]) <= porc:
			print(f'[ 2 ] Nome: {pycolor.green()}{init2[0]}{pycolor.nill()}  Vidas: {pycolor.red(5)}{init2[4]}{pycolor.nill()}/{init2[3]}  Cidade: {init2[22]}')
		else:
			print(f'[ 2 ] Nome: {pycolor.green()}{init2[0]}{pycolor.nill()}  Vidas: {pycolor.green()}{init2[4]}{pycolor.nill()}/{init2[3]}  Cidade: {init2[22]}')
	if init3 == []:
		print(f'[ 3 ] {pycolor.white(3)}Arquivo vazio.{pycolor.nill()}')
	elif init3 != []:
		if int(init3[3]) <= porc:
			print(f'[ 3 ] Nome: {pycolor.green()}{init3[0]}{pycolor.nill()}  Vidas: {pycolor.red(5)}{init3[4]}{pycolor.nill()}/{init3[3]}  Cidade: {init3[22]}')
		else:
			print(f'[ 3 ] Nome: {pycolor.green()}{init3[0]}{pycolor.nill()}  Vidas: {pycolor.green()}{init3[4]}{pycolor.nill()}/{init3[3]}  Cidade: {init3[22]}')
	res = uteis.inint('Sua escolha: ')
	if res == 1:
		if init1 != []:
			title('\033[31mCuidado, já existe um arquivo salvo, deseja sobreescrever?\033[m')
			sleep(2)
			print('[ 1 ] Sim\n[ 2 ] Não')
			res = uteis.inint('Sua escolha: ')
			if res == 1:
				save(1)
				title('\033[32mSALVANDO...\033[m')
				sleep(2)
				title('\033[32mSalvo com sucesso.\033[m')
				sleep(2)
				del init1[:], init2[:], init3[:]
				uteis.clear()
		else:
			save(1)
			title('\033[32mSALVANDO...\033[m')
			sleep(2)
			title('\033[32mSalvo com sucesso.\033[m')
			sleep(2)
			del init1[:], init2[:], init3[:]
			uteis.clear()
	elif res == 2:
		if init2 != []:
			title('\033[31mCuidado, já existe um arquivo salvo, deseja sobreescrever?\033[m')
			sleep(2)
			print('[ 1 ] Sim\n[ 2 ] Não')
			res = uteis.inint('Sua escolha: ')
			if res == 1:
				save(2)
				title('\033[32mSALVANDO...\033[m')
				sleep(2)
				title('\033[32mSalvo com sucesso.\033[m')
				sleep(2)
				del init1[:], init2[:], init3[:]
				uteis.clear()
		else:
			save(2)
			title('\033[32mSALVANDO...\033[m')
			sleep(2)
			title('\033[32mSalvo com sucesso.\033[m')
			sleep(2)
			del init1[:], init2[:], init3[:]
			uteis.clear()
	elif res == 3:
		if init3 != []:
			title('\033[31mCuidado, já existe um arquivo salvo, deseja sobreescrever?\033[m')
			sleep(2)
			print('[ 1 ] Sim\n[ 2 ] Não')
			res = uteis.inint('Sua escolha: ')
			if res == 1:
				save(3)
				title('\033[32mSALVANDO...\033[m')
				sleep(2)
				title('\033[32mSalvo com sucesso.\033[m')
				sleep(2)
				del init1[:], init2[:], init3[:]
				uteis.clear()
		else:
			save(3)
			title('\033[32mSALVANDO...\033[m')
			sleep(2)
			title('\033[32mSalvo com sucesso.\033[m')
			sleep(2)
			del init1[:], init2[:], init3[:]
			uteis.clear()
	else:
		erro()

#-----------------------------------------------------------------------------------


#---------------------------- Programa Principal -----------------------------------
title(f'\033[1;33mFANTASY\033[m {pycolor.red(1)}EMPIRES{pycolor.nill()}', '=')
sleep(2)
print(f'{pycolor.green()}{"As quatro torres":^31}{pycolor.nill()}')
print('-' * 31)
#------------------------ VARIAVEIS ----------------------------
nome = ''
nev = 'False'
fim = 'False'
jlifesmax = 12
jlifes = jlifesmax
#---------------------------
glife = pycolor.green()
blife = pycolor.red(5)
porc = (jlifesmax * 42) // 100
#---------------------------
totex = 0
ni = 1
maxex = 12
arefl = 'False'
lamp = 'False'
dmin = 1
dmax = 3
luz = 'False'
sod = 'False'
#--- enemys ----
alifesmax = 8
alifes = alifesmax
llifesmax = 99
llifes = llifesmax
#---------------
gameover = 'False'
stage1 = 'True'
stage2 = 'True'
stage3 = 'False'
mapa = 'False'
money = 0
pocao = 0
esp = 'False'
elf = 'False'
city = ''
rpas = 'False'
resp = 'False'
zan = 'False'
stage4 = 'False'
ctot = 'False'
#------------------------ INICIALIZAÇÃO DO JOGO ----------------------------
print('[ 1 ] Continuar\n[ 2 ] Novo jogo')
res = uteis.inint('Sua escolha: ')
if res == 1:
	while True:
		uteis.clear()
		viw(1)
		viw(2)
		viw(3)
		print('Abrir qual arquivo?')
		print('-'*30)
		if init1 == []:
			print(f'[ 1 ] {pycolor.white(3)}Arquivo vazio.{pycolor.nill()}')
		else:
			if int(init1[4]) <= porc:
				print(f'[ 1 ] Nome: {pycolor.green()}{init1[0]}{pycolor.nill()}  Vidas: {pycolor.red(5)}{init1[4]}{pycolor.nill()}/{init1[3]}  Cidade: {init1[22]}')
			else:
				print(f'[ 1 ] Nome: {pycolor.green()}{init1[0]}{pycolor.nill()}  Vidas: {pycolor.green()}{init1[4]}{pycolor.nill()}/{init1[3]}  Cidade: {init1[22]}')
		if init2 == []:
			print(f'[ 2 ] {pycolor.white(3)}Arquivo vazio.{pycolor.nill()}')
		elif init2 != []:
			if int(init2[4]) <= porc:
				print(f'[ 2 ] Nome: {pycolor.green()}{init2[0]}{pycolor.nill()}  Vidas: {pycolor.red(5)}{init2[4]}{pycolor.nill()}/{init2[3]}  Cidade: {init2[22]}')
			else:
				print(f'[ 2 ] Nome: {pycolor.green()}{init2[0]}{pycolor.nill()}  Vidas: {pycolor.green()}{init2[4]}{pycolor.nill()}/{init2[3]}  Cidade: {init2[22]}')
		if init3 == []:
			print(f'[ 3 ] {pycolor.white(3)}Arquivo vazio.{pycolor.nill()}')
		elif init3 != []:
			if int(init3[4]) <= porc:
				print(f'[ 3 ] Nome: {pycolor.green()}{init3[0]}{pycolor.nill()}  Vidas: {pycolor.red(5)}{init3[4]}{pycolor.nill()}/{init3[3]}  Cidade: {init3[22]}')
			else:
				print(f'[ 3 ] Nome: {pycolor.green()}{init3[0]}{pycolor.nill()}  Vidas: {pycolor.green()}{init3[4]}{pycolor.nill()}/{init3[3]}  Cidade: {init3[22]}')
		cp = uteis.inint('Sua escolha: ')
		if cp == 1 and init1 != []:
			change(1)
			print('\033[mCARREGANDO JOGO...')
			sleep(2)
			uteis.clear()
			break
		elif cp == 2 and init2 != []:
			change(2)
			print('\033[mCARREGANDO JOGO...')
			sleep(2)
			uteis.clear()
			break
		elif cp == 3 and init3 != []:
			change(3)
			print('\033[mCARREGANDO JOGO...')
			sleep(2)
			uteis.clear()
			break
		else:
			erro()
elif res == 2:
	print('\033[mINICIANDO NOVO JOGO...')
	sleep(2)
	uteis.clear()
else:
	erro()
#---------------------- JOGO (EM CONSTRUÇÃO) ------------------------
if res >= 2:
	title('\033[37mAntes de começar o jogo eu quero saber seu nome:\033[m')
	sleep(2)
	while True:
		nome = input('Qual o seu nome?\033[32m ')
		print('\033[m')
		if len(nome) <= 12:
			break
		else:
			title('\033[37mSeu nome só pode ter até 12 caracteres.\033[m')
			sleep(2)
	title('\033[37mObrigado, agora podemos começar o jogo.\033[m')
	sleep(3)
	uteis.clear()
while True:
	if fim == 'True':
		break
	if gameover == 'True':
		break
#------------------------ ESTÁGIO 1 (CONCLUIDO) ----------------------------
	while True:
		if gameover == 'True':
			break
		if stage1 == 'False':
			break
		city = 'Kanaghin'
		title('\033[34mVocê esta em sua casa, sentado na cama, o que você vai fazer?\033[m')
		sleep(2)
		print('[ 1 ] Sair da casa\n[ 2 ] Dormir\n[ 3 ] Pular na cama')
		res = uteis.inint('Sua escolha: ')
		uteis.clear()
		if res == 1:
			title('\033[34mA porta está trancada, você nota um buraco no chão. E agora?\033[m')
			sleep(2)
			while True:
				print('[ 1 ] Voltar a cama\n[ 2 ] Ver o que tem no buraco\n[ 3 ] Bater na porta')
				res = uteis.inint('Sua escolha: ')
				uteis.clear()
				if res == 1:
					break
				elif res == 2:
					title('Você coloca a mão, \033[31muma aranha atacou!\033[m')
					sleep(2)
					while True:
						uteis.clear()
						sprites.aranha('\033[41m')
						if jlifes <= porc:
							title(f'Aranha: {alifes}/8  Você: {blife}{jlifes}{pycolor.nill()}/12')
						else:
							title(f'Aranha: {alifes}/8  Você: {glife}{jlifes}{pycolor.nill()}/12')
						print('[ 1 ] Atacar\n[ 2 ] defender')
						res = uteis.inint('Sua escolha: ')
						if res == 1:
							dano = randint(1,3)
							title(f'\033[33mVocê atacou a aranha! tirou {dano} de vida.\033[m')
							alifes -= dano
							sleep(2)
						elif res == 2:
							stitle('Você espera a aranha.')
							sleep(2)
						else:
							print('\033[31mERRO. TENTE NOVAMENTE.\033[m')
						if alifes <= 0:
							title('\033[33mVocê derrotou a aranha!\033[m')
							sleep(2)
							uteis.clear()
							break
						if res <= 2:
							if res == 2:
								dano = randint(0,2)
							else:
								dano = randint(1,3)
							if dano == 0:
								title('\033[33mA aranha errou!\033[m')
							else:
								title(f'\033[31mA aranha atacou! tirou {dano} de vida.\033[m')
							sleep(2)
							jlifes -= dano
						if jlifes <= 0:
							title('\033[31mVocê perdeu!\033[m')
							sleep(2)
							print('\033[1;31mGAME OVER!\033[m')
							sleep(2)
							gameover = 'True'
							break
					if gameover == 'True':
						break
					title('\033[32mVocê conseguiu uma chave.\033[m')
					sleep(2)
					alifes = 8
					print('[ 1 ] Abrir porta\n[ 2 ] Jogar chave fora')
					res = uteis.inint('Sua escolha: ')
					uteis.clear()
					if res == 1:
						title('\033[34mVocê saiu da sua casa!\033[m')
						sleep(2)
						ni = 2
						jlifesmax = (ni-1) * 2 + 12
						dmin = (ni-1) + 1
						dmax = (ni-1) + 1
						porc = (jlifesmax * 42) // 100
						title(f'\033[32mVocê subiu para o nivel {ni}!!!\033[m')
						sleep(2)
						stage1 = 'False'
						break
					elif res == 2:
						title('\033[34mVocê jogou a chave fora, mas não se preocupe ela caiu no buraco.\033[m')
						sleep(2)
					else:
						erro()
				elif res == 3:
					title('\033[34mVocê bate na porta, ela é muito dura!\033[m')
					sleep(2)
				else:
					erro()
		elif res == 2:
			title('\033[31mVocê não pode dormir agora!\033[m')
			sleep(2)
		elif res == 3:
			title('\033[34mA cama se quebrou! Você caiu no chão e desmaiou.\033[m')
			sleep(2)
			print('\033[1;31mGAME OVER!\033[m')
			sleep(2)
			gameover = 'True'
		else:
			erro()
#------------------------ ESTÁGIO 2 (CONCLUIDO) ----------------------------
	while True:
		city = 'Kanaghin'
		if stage2 == 'False':
			break
		if gameover == 'True':
			break
		while True:
			if stage2 == 'False':
				break
			if gameover == 'True':
				break
			uteis.clear()
			title('\033[34mVocê está em uma rua de uma vila da era medieval chamada Kanaghin.\033[m')
			sleep(2)
			title('\033[34mNa rua, uma pessoa está andando de lá para cá.\033[m')
			sleep(2)
			print('[ 1 ] Voltar para casa\n[ 2 ] Falar com a pessoa\n[ 3 ] Ver mais da vila')
			res = uteis.inint('Sua escolha: ')
			uteis.clear()
			if res == 999:
				menuj()
			elif res == 1:
				while True:
					if stage2 == 'False':
						break
					if gameover == 'True':
						break
					title('\033[34mVocê entrou na sua casa, a mesma de sempre.\033[m')
					sleep(2)
					print('[ 1 ] Sair da casa\n[ 2 ] Dormir\n[ 3 ] Ir para o diário')
					res = uteis.inint('Sua escolha: ')
					uteis.clear()
					if res == 999:
						menuj()
					elif res == 1:
						break
					elif res == 2:
						if jlifes < jlifesmax:
							title('\033[32mDormiu como pedra...\033[m')
							jlifes = jlifesmax
							sleep(2)
							title('\033[32mVocê recuperou energia!\033[m')
							sleep(2)
						else:
							title('\033[31mVocê não pode dormir agora!\033[m')
							sleep(2)
					elif res == 3:
						tsave()
					else:
						erro()
			elif res == 2:
				title('\033[32mPESSOA: Olá, eu sou Fang.\033[m')
				sleep(2)
				title('\033[32mFang: Eu posso ensinar algumas coisas sobre o jogo\033[m')
				sleep(2)
				while True:
					title('\033[32mFang: Como posso ajudar?\033[m')
					sleep(2)
					print('[ 1 ] Itens da casa\n[ 2 ] Menu\n[ 3 ] Nada')
					res = uteis.inint('Sua escolha: ')
					uteis.clear()
					if res == 1:
						title('\033[32mFang: Qual item?\033[m')
						sleep(2)
						while True:
							print('[ 1 ] Cama\n[ 2 ] Diário\n[ 3 ] Nada')
							res = uteis.inint('Sua escolha: ')
							uteis.clear()
							if res == 1:
								title('\033[32mFang: Você pode usar a cama para recuperar energia.\033[m')
								sleep(2)
								title('\033[32mFang: Você perde energia quando é atacado numa batalha.\033[m')
								sleep(2)
							elif res == 2:
								title('\033[32mFang: Esse é o diario do qual você pode salvar seu jogo.\033[m')
								sleep(2)
							elif res == 3:
								break
							else:
								erro()
					elif res == 2:
						title('\033[32mFang: No menu você vê os itens que possue.\033[m')
						sleep(2)
						title('\033[32mFang: Para acessar o menu, basta digitar 999 nas opções.\033[m')
						sleep(2)
						title('\033[32mFang: Para sair do menu digite novamente 999.\033[m')
						sleep(2)
						title('\033[32mFang: Vamos, teste.\033[m')
						sleep(2)
						print('[ 1 ] blá\n[ 2 ] blá blá')
						res = uteis.inint('Sua escolha: ')
						if res == 999:
							menuj()
						title('\033[32mFang: Parabéns, você entendeu.\033[m')
						sleep(2)
						if mapa == 'True':
							title('\033[32mFang: Vejo que você tem um mapa!.\033[m')
							sleep(2)
							title('\033[32mFang: Para acessar o mapa, basta digitar o número à esquerda do item.\033[m')
							sleep(2)
							title('\033[32mFang: Com o mapa você pode viajar a outras cidades.\033[m')
							sleep(2)
							title('\033[32mFang: Como recompensa, lhe darei isso.\033[m')
							sleep(2)
							title('\033[33mVocê ganhou mapa da cidade Nevada.\033[m')
							nev = 'True'
					elif res == 3:
						break
					else:
						erro()
			elif res == 3:
				while True:
					if stage2 == 'False':
						break
					title('\033[34mExite algumas casas na vila, uma a sua direita outra a esquerda.\033[m')
					sleep(2)
					title('\033[34mExite também uma hospedaria na frente da casa.\033[m')
					sleep(2)

					print('[ 1 ] Casa da direita\n[ 2 ] Hospedaria\n[ 3 ] Casa da esquerda\n[ 4 ] Voltar')
					res = uteis.inint('Sua escolha: ')
					uteis.clear()
					if res == 999:
						menuj()
					elif res == 1:
						if elf == 'False':
							title('\033[34mDentro da casa tem apenas um baú.\033[m')
							sleep(2)
							title('\033[34mDentro do baú você encontrou um elfo!.\033[m')
							sleep(2)
							title('\033[32mElfo: Obrigado por me libertar, lhe darei isso como recompensa.\033[m')
							sleep(2)
							money += 200
							title('\033[32mVocê ganhou 200 Moedas!!!\033[m')
							sleep(3)
							elf = 'True'
							uteis.clear()
						else:
							title('\033[34mEstá trancada.\033[m')
							sleep(2)
					elif res == 2:
						if arefl == 'False':
							title('\033[34mVocê precisa ter um arco e flecha para entrar.\033[m')
							sleep(2)
						else:
							title('\033[34mVocê entra na hospedaria, lá tem 3 pessoas sentadas comendo.\033[m')
							sleep(2)
							while True:
								if stage2 == 'False':
									break
								print('[ 1 ] Falar com Pessoa 1\n[ 2 ] Falar com Pessoa 2\n[ 3 ] Falar com Pessoa 3\n[ 4 ] Ver mais da hospedaria\n[ 5 ] Sair')
								res = uteis.inint('Sua escolha: ')
								uteis.clear()
								if res == 999:
									menuj()
								elif res == 1:
									title('\033[35mPESSOA 1: Nhoc, nhoc,nhoc...\033[m')
									sleep(2)
								elif res == 2:
									title('\033[36mPESSOA 2: Zzzzzzzzz...\033[m')
									sleep(2)
								elif res == 3:
									title('\033[32mPESSOA 3: Olá, você deve ser novo por aqui\033[m')
									sleep(1)
									title('\033[32mPESSOA 3: Eu sou um soldado do castelo de Nevada.\033[m')
									sleep(2)
									while True:
										print('[ 1 ] Castelo de Nevada?\n[ 2 ] O que você está fazendo aqui?\n[ 3 ] Ok')
										res = uteis.inint('Sua escolha: ')
										uteis.clear()
										if res == 1:
											title('\033[32mPESSOA 3: É o castelo que fica na capital Nevada, ao norte.\033[m')
											sleep(2)
										elif res == 2:
											title('\033[32mPESSOA 3: É confidencial, desculpe.\033[m')
											sleep(2)
										elif res == 3:
											title('\033[32mPESSOA 3: Até mais!\033[m')
											break
										else:
											erro()
								elif res == 4:
									if llifes > 0:
										title('\033[34mVocê contiuna andando e percebe o dono da hospedaria no balcão.\033[m')
										sleep(2)
										title('\033[34mEle começa a falar com você sobre um monte de coisas.\033[m')
										sleep(2)
										title('\033[34mEnquanto vocês conversam, o soldado sai da hospedaria.\033[m')
										sleep(2)
										title('\033[34mDe repente, uma pessoa chega e anucia um assalto. E agora?\033[m')
										sleep(2)
										print('[ 1 ] Atacar\n[ 2 ] Esperar')
										res = uteis.inint('Sua escolha: ')
										uteis.clear()
										if res == 1:
											title('\033[34mVocê o atacou! Hora da batalha!!!\033[m')
											sleep(2)
											while True:
												uteis.clear()
												sprites.ladrao()
												if jlifes <= porc:
													title(f'Ladrão: {llifes}/{llifesmax}  Você: {blife}{jlifes}{pycolor.nill()}/{jlifesmax}')
												else:
													title(f'Ladrão: {llifes}/{llifesmax}  Você: {glife}{jlifes}{pycolor.nill()}/{jlifesmax}')
												print('[ 1 ] Atacar\n[ 2 ] defender')
												res = uteis.inint('Sua escolha: ')
												if res == 1:
													stitle('>>> ITEM <<<')
													if resp == 'False':
														print('[ 1 ] Soco\n[ 2 ] arco e flecha')
													else:
														print('[ 1 ] Rangnarok\n[ 2 ] arco e flecha')
													resm = uteis.inint('Sua escolha: ')
													if resm == 1:
														if resp == 'False':
															dano = randint(dmin, dmax)
															title(f'\033[33mVocê atacou o ladrão! tirou {dano} de vida.\033[m')
															llifes -= dano
														else:
															dano = llifesmax
															title(f'\033[33mVocê atacou o ladrão! tirou {dano} de vida.\033[m')
															llifes = 0
														sleep(2)
													elif resm == 2:
														dano = randint(dmin+2, dmax+2)
														title(f'\033[33mVocê acertou uma flecha no ladrão! tirou {dano} de vida.\033[m')
														llifes -= dano
														sleep(2)
												elif res == 2:
													stitle('Você espera o ladrão.')
													sleep(2)
												else:
													print('\033[31mERRO. TENTE NOVAMENTE.\033[m')
												if llifes <= 0:
													title('\033[33mVocê derrotou o ladrão!\033[m')
													resp = 'False'
													sleep(2)
													title('\033[31mA espada sumiu!\033[m')
													sleep(2)
													ex = randint(5,7)
													title(f'\033[32mVocê ganhou {ex} de experiencia!\033[m')
													totex += ex
													sleep(2)
													lvup()
													uteis.clear()
													break
												elif res <= 2:
													if res == 2:
														dano = randint(0,3)
													else:
														dano = randint(4,10)
													if dano == 0:
														title('\033[33mO ladrão errou!\033[m')
													else:
														title(f'\033[31mO ladrão atacou! tirou {dano} de vida.\033[m')
														sleep(2)
														jlifes -= dano
														if jlifes <= 5:
															title('\033[35mDesconhecido: Ei, tome isso.\033[m')
															sleep(2)
															title('\033[32mGanhou Ragnarok!\033[m')
															sleep(2)
															resp = 'True'
												if jlifes <= 0:
													title('\033[31mVocê perdeu!\033[m')
													sleep(2)
													print('\033[1;31mGAME OVER!\033[m')
													sleep(2)
													gameover = 'True'
													break
											if gameover == 'True':
												break
										if gameover == 'True':
											break
										elif res == 2:
											title('\033[34mVocê conseque fugir do ladrão!\033[m')
											sleep(2)
											break
											
										elif llifes <= 0:
											title('\033[32mDono: Obrigado por impedir o ladrão!!!\033[m')
											sleep(2)
											title('\033[32mDono: Eu nao sei como lhe agradecer.\033[m')
											sleep(2)
											title('\033[32mDono: Eu só posso lhe oferecer isso...\033[m')
											sleep(2)
											title('\033[33mVocê ganhou mapa! Use-o no menu.\033[m')
											mapa = 'True'
											sleep(3)
											title('\033[34mPara saber como usar o mapa fale com Fang\033[m')
											sleep(2)
									else:
										title('\033[32mDono: Obrigado de novo por impedir o ladrão!!!\033[m')
										sleep(2)
										title('\033[32mDono: Você gostou do presente?\033[m')
										sleep(2)
								elif res == 5:
									title('\033[33m>>> VOLTE SEMPRE!!! <<<\033[m')
									sleep(2)
									break
								else:
									erro()
								if gameover == 'True':
									break
							if gameover == 'True':
								break
					elif res == 3 and arefl == 'False':
						title('\033[34mVocê entra na casa e um senhor te recebe.\033[m')
						sleep(2)
						title('\033[36mPESSOA: Olá, eu sou Gus, o treinador, e aqui é o centro de torneios.\033[m')
						sleep(2)
						title('\033[36mGus: Deseja competir?\033[m')
						sleep(2)
						print('[ 1 ] Sim\n[ 2 ] Não')
						res = uteis.inint('Sua escolha: ')
						uteis.clear()
						if res == 1:
							title('\033[36mGus: Deseja que lhe ensine como funciona o torneio?\033[m')
							sleep(2)
							print('[ 1 ] Sim\n[ 2 ] Não')
							res = uteis.inint('Sua escolha: ')
							uteis.clear()
							if res == 1:
								title('\033[36mGus: O torneio é um total de 3 batalhas com oponentes.\033[m')
								sleep(2)
								title('\033[36mGus: Se você consequir vencer todas ganha um prêmio.\033[m')
								sleep(2)
								title('\033[36mGus: Vamos começar.\033[m')
								sleep(2)
							elif res == 2:
								title('\033[36mGus: Vamos começar.\033[m')
								sleep(2)
							else:
								erro()
							print('>>> PRIMEIRA BATALHA <<<')
							sleep(2)
							while True:
								uteis.clear()
								sprites.aranha('\033[41m')
								if jlifes <= porc:
									title(f'Aranha: {alifes}/{alifesmax}  Você: {blife}{jlifes}{pycolor.nill()}/{jlifesmax}')
								else:
									title(f'Aranha: {alifes}/{alifesmax}  Você: {glife}{jlifes}{pycolor.nill()}/{jlifesmax}')
								print('[ 1 ] Atacar\n[ 2 ] defender')
								res = uteis.inint('Sua escolha: ')
								if res == 1:
									dano = randint(dmin, dmax)
									title(f'\033[33mVocê atacou a aranha! tirou {dano} de vida.\033[m')
									alifes -= dano
									sleep(2)
								elif res == 2:
									stitle('Você espera a aranha.')
									sleep(2)
								else:
									erro()
								if alifes <= 0:
									title('\033[33mVocê derrotou a aranha!\033[m')
									sleep(2)
									ex = randint(2,3)
									title(f'\033[32mVocê ganhou {ex} de experiencia!\033[m')
									totex += ex
									sleep(2)
									if totex >= maxex:
										ni += 1
										title(f'\033[32mVocê subiu para o nivel {ni}!!!\033[m')
										sleep(2)
										jlifesmax += 2
										title(f'\033[32mSua energia aumentou em 2!\033[m')
										sleep(2)
									uteis.clear()
									break
								if res <= 2:
									if res == 2:
										dano = randint(0,2)
									else:
										dano = randint(1,3)
									if dano == 0:
										title('\033[33mA aranha errou!\033[m')
									else:
										title(f'\033[31mA aranha atacou! tirou {dano} de vida.\033[m')
									sleep(2)
									jlifes -= dano
								if jlifes <= 0:
									title('\033[31mVocê perdeu!\033[m')
									sleep(2)
									print('\033[1;31mGAME OVER!\033[m')
									sleep(2)
									gameover = 'True'
									break
							if gameover == 'True':
								break
							title('\033[36mGus: Parabens, você ganhou a primeira partida.\033[m')
							sleep(2)
							title('\033[36mGus: Agora descanse um pouco.\033[m')
							sleep(2)
							jlifes = jlifesmax
							title('\033[32mVocê recuperou sua energia!\033[m')
							sleep(2)
							print('>>> SEGUNDA BATALHA <<<')
							sleep(2)
							alifes = alifesmax + 2
							while True:
								uteis.clear()
								sprites.aranha('\033[42m')
								if jlifes <= porc:
									title(f'Aranha media: {alifes}/{alifesmax + 2}  Você: {blife}{jlifes}{pycolor.nill()}/{jlifesmax}')
								else:
									title(f'Aranha media: {alifes}/{alifesmax + 2}  Você: {glife}{jlifes}{pycolor.nill()}/{jlifesmax}')
								print('[ 1 ] Atacar\n[ 2 ] defender')
								res = uteis.inint('Sua escolha: ')
								if res == 1:
									dano = randint(dmin,dmax)
									title(f'\033[33mVocê atacou a aranha! tirou {dano} de vida.\033[m')
									alifes -= dano
									sleep(2)
								elif res == 2:
									stitle('Você espera a aranha.')
									sleep(2)
								else:
									print('\033[31mERRO. TENTE NOVAMENTE.\033[m')
								if alifes <= 0:
									title('\033[33mVocê derrotou a aranha!\033[m')
									sleep(2)
									ex = randint(3,4)
									title(f'\033[32mVocê ganhou {ex} de experiencia!\033[m')
									totex += ex
									sleep(2)
									if totex >= maxex:
										ni += 1
										title(f'\033[32mVocê subiu para o nivel {ni}!!!\033[m')
										sleep(2)
										jlifesmax += 2
										title(f'\033[32mSua energia aumentou em 2!\033[m')
										sleep(2)
									uteis.clear()
									break
								if res <= 2:
									if res == 2:
										dano = randint(1,2)
									else:
										dano = randint(2,3)
									if dano == 0:
										title('\033[33mA aranha errou!\033[m')
									else:
										title(f'\033[31mA aranha atacou! tirou {dano} de vida.\033[m')
									sleep(2)
									jlifes -= dano
								if jlifes <= 0:
									title('\033[31mVocê perdeu!\033[m')
									sleep(2)
									print('\033[1;31mGAME OVER!\033[m')
									sleep(2)
									gameover = 'True'
									break
							if gameover == 'True':
								break
							title('\033[36mGus: Parabens, você ganhou a segunda partida.\033[m')
							sleep(2)
							title('\033[36mGus: Agora descanse um pouco.\033[m')
							sleep(2)
							jlifes = jlifesmax
							title('\033[32mVocê recuperou sua energia!\033[m')
							sleep(2)
							print('>>> TERCEIRA BATALHA <<<')
							sleep(2)
							alifes = alifesmax + 4
							while True:
								uteis.clear()
								sprites.aranha('\033[43m', '\033[41m')
								if jlifes <= porc:
									title(f'Aranha grande: {alifes}/{alifesmax + 4}  Você: {blife}{jlifes}{pycolor.nill()}/{jlifesmax}')
								else:
									title(f'Aranha grande: {alifes}/{alifesmax + 4}  Você: {glife}{jlifes}{pycolor.nill()}/{jlifesmax}')
								print('[ 1 ] Atacar\n[ 2 ] defender')
								res = uteis.inint('Sua escolha: ')
								if res == 1:
									dano = randint(dmin,dmax)
									title(f'\033[33mVocê atacou a aranha! tirou {dano} de vida.\033[m')
									alifes -= dano
									sleep(2)
								elif res == 2:
									stitle('Você espera a aranha.')
									sleep(2)
								else:
									print('\033[31mERRO. TENTE NOVAMENTE.\033[m')
								if alifes <= 0:
									title('\033[33mVocê derrotou a aranha!\033[m')
									sleep(2)
									ex = randint(3,4)
									title(f'\033[32mVocê ganhou {ex} de experiencia!\033[m')
									totex += ex
									sleep(2)
									if totex >= maxex:
										ni += 1
										title(f'\033[32mVocê subiu para o nivel {ni}!!!\033[m')
										sleep(2)
										jlifesmax += 2
										title(f'\033[32mSua energia aumentou em 2!\033[m')
										sleep(2)
									uteis.clear()
									break
								if res <= 2:
									if res == 2:
										dano = randint(1,2)
									else:
										dano = randint(2,3)
									if dano == 0:
										title('\033[33mA aranha errou!\033[m')
									else:
										title(f'\033[31mA aranha atacou! tirou {dano} de vida.\033[m')
									sleep(2)
									jlifes -= dano
								if jlifes <= 0:
									title('\033[31mVocê perdeu!\033[m')
									sleep(2)
									print('\033[1;31mGAME OVER!\033[m')
									sleep(2)
									gameover = 'True'
									break
							if gameover == 'True':
								break
							title('\033[36mGus: Parabens, você ganhou o torneio.\033[m')
							sleep(2)
							title('\033[36mGus: O prêmio é: um arco e flecha e 500 Moedas!\033[m')
							arefl = True
							money += 500
							sleep(2)
							title('\033[36mGus: Volte sempre!!!.\033[m')
							sleep(2)
							uteis.clear()
						elif res == 2:
							title('\033[36mGus: Então até mais.\033[m')
							sleep(2)
						else:
							erro()
					elif res == 3 and arefl == 'True':
						title('\033[34mEstá trancada.\033[m')
						sleep(2)
					elif res == 4:
						break
					else:
						erro()
			else:
				erro()
#------------------------ ESTÁGIO 3 (CONCLUIDO) ----------------------------
	while True:
		city = 'Nevada'
		if gameover == 'True':
			break
		if stage3 == 'False':
			break
		while True:
			if stage3 == 'False':
				break
			if gameover == 'True':
				break
			title('\033[34mVocê está na capital do reino, Nevada\033[m')
			sleep(2)
			title('\033[34mExistem varias casas ao redor\033[m')
			sleep(2)
			title('\033[34mTalvez você possa entrar em algumas\033[m')
			sleep(2)
			print('[ 1 ] Casa 1\n[ 2 ] Casa 2\n[ 3 ] Casa 3\n[ 4 ] Ver mais da cidade')
			res = uteis.inint('Sua escolha: ')
			uteis.clear()
			if res == 999:
				menuj()
			elif res == 1:
				title('\033[35mAldeão: Olá, eu sou apenas um aldeão solitário...\033[m')
				sleep(2)
			elif res == 2:
				title('\033[36mAldeão 2: Hum? Quem é você?\033[m')
				sleep(2)
				print('[ 1 ] Ninguem\n[ 2 ] Um aventureiro')
				res = uteis.inint('Sua escolha: ')
				uteis.clear()
				if res == 1:
					title('\033[36mAldeão 2: Hum? Então saia daqui!!!\033[m')
					sleep(2)
				elif res == 2:
					if lamp == 'False':
						title('\033[36mAldeão 2: Hum? Então entre! Eu tenho algo para você.\033[m')
						sleep(2)
						title('\033[36mAldeão 2: Tome, eu já ia da-lo a qualquer um mesmo.\033[m')
						sleep(2)
						title('\033[36mAldeão 2: Eu não sei para que serve.\033[m')
						sleep(2)
						title('\033[32mGanhou lampião!!!\033[m')
						sleep(2)
						uteis.clear()
						lamp = 'True'
						sleep(2)
					else:
						title('\033[36mAldeão 2: Hum? Não tenho mais nada para você.\033[m')
						sleep(2)
				else:
					erro()
			elif res == 3:
				if sod == 'False':
					title('\033[34mEstá trancada... Que pena.\033[m')
					sleep(2)
				else:
					title('\033[32mBart: Olá, bem vindo à minha casa, você está pronto para ir?\033[m')
					sleep(2)
					print('[ 1 ] Sim!!! Vamos lá\n[ 2 ] Não, ainda não...')
					res = uteis.inint('Sua escolha: ')
					uteis.clear()
					if res == 1:
						title('\033[32mA missão consiste em ir até o reino de Mililand.\033[m')
						sleep(2)
						title('\033[32mDe lá, nós iremos procurar o rei Ferg.\033[m')
						sleep(2)
						title('\033[32mTome, isso irá te ajudar.\033[m')
						sleep(2)
						title('\033[32mGANHOU MAPA PARA MILILAND.\033[m')
						zan = 'True'
						sleep(2)
						uteis.clear()
					elif res == 2:
						title('\033[32mBart: Tudo bem, lhe vejo mais tarde.\033[m')
						sleep(2)
					else:
						erro()
			elif res == 4:
				title('\033[34mExistem mais 2 casas, uma loja, e um castelo.\033[m')
				sleep(2)
				while True:
					if stage3 == 'False':
						break
					if gameover == 'True':
						break
					print('[ 1 ] Voltar\n[ 2 ] Casa 4\n[ 3 ] Casa 5\n[ 4 ] Loja\n[ 5 ] Castelo')
					res = uteis.inint('Sua escolha: ')
					uteis.clear()
					if res == 999:
						menuj()
					elif res == 1:
						break
					elif res == 2:
						title('\033[34mPESSOA 4: Eu ouvi dizer que ao leste daqui existe uma cidade abandonada\033[m')
						sleep(2)
						title('\033[34mPESSOA 4: Ela se chamava totalis, mas niguem sabe como chegar lá...\033[m')
						sleep(2)
					elif res == 3:
						title('\033[32mPESSOA 5: Eu acho que tem algo errado no castelo...\033[m')
						sleep(2)
					elif res == 4:
						while True:
							if stage3 == 'False':
								break
							if gameover == 'True':
								break
							uteis.clear()
							title('\033[33mBem vindo à loja da capital.\033[m')
							sleep(2)
							title('\033[33mAqui você pode comprar itens para usar no menu.\033[m')
							sleep(2)
							title('\033[33mO que você vai quer?\033[m')
							if esp == 'False':
								print('[ 1 ] Poção\n[ 2 ] Espada\n[ 3 ] Nada')
							else:
								print('[ 1 ] Poção\n[ 3 ] Nada')
							res = uteis.inint('Sua escolha: ')
							uteis.clear()
							if res == 999:
								menuj()
							elif res == 1:
								if money == 0:
									title('\033[33mQue pena... Você não tem dinheiro.\033[m')
									sleep(2)
									title('\033[33mInfelizmente você não pode comprar nada.\033[m')
									sleep(2)
									break
								else:
									title('\033[33mO preço de 1 poção é: 50 Moedas.\033[m')
									sleep(2)
									title('\033[33mQuantas poções você vai querer?\033[m')
									sleep(2)
									quant = uteis.inint('Sua escolha: ')
									preco = 50 * quant
									if quant == 1:
										title(f'\033[33mO preço de {quant} poção é de {preco} Moedas.\033[m')
									else:
										title(f'\033[33mO preço de {quant} poções é de {preco} Moedas.\033[m')
									sleep(2)
									title(f'\033[33mDeseja continuar?\033[m')
									print('[ 1 ] Sim\n[ 2 ] Não')
									res = uteis.inint('Sua escolha: ')
									uteis.clear()
									if res == 1:
										if preco > money:
											title(f'\033[31mDinheiro insuficiente.\033[m')
											sleep(2)
										else:
											money -= preco
											pocao += quant
											title(f'\033[33mCompra realizada com sucesso.\033[m')
											sleep(2)
							elif res == 2 and esp == 'False':
								if rpas == 'False':
									title('\033[33mEssa espada estranha custa 10.000 Moedas.\033[m')
									sleep(2)
									title('\033[33mVai comprar?\033[m')
									print('[ 1 ] Sim\n[ 2 ] Não')
									res = uteis.inint('Sua escolha: ')
									uteis.clear()
									if res == 1:
										title('\033[33mQue pena, você não tem dinheiro suficiente.\033[m')
										sleep(2)
									elif res == 2:
										title('\033[33mOk, veja outros produtos.\033[m')
										sleep(2)
								else:
									title('\033[33mVocê tem um passe! Eu lhe darei essa espada.\033[m')
									sleep(2)
									title('\033[32mGanhou espada ragnarok!!!\033[m')
									esp = 'True'
									sleep(2)
							elif res == 3:
								title('\033[33mVolte sempre!!!\033[m')
								sleep(2)
								break
					elif res == 5:
						while True:
							if gameover == 'True':
								break
							title('\033[34mVocê está indo até o castelo da cidade.\033[m')
							sleep(2)
							title('\033[34mVocê entra no castelo, existem três portas no salão.\033[m')
							sleep(2)
							title('\033[34mE agora?\033[m')
							sleep(2)
							print('[ 1 ] Porta 1\n[ 2 ] Porta 2\n[ 3 ] Porta 3\n[ 4 ] Sair')
							res = uteis.inint('Sua escolha: ')
							uteis.clear()
							if res == 999:
								title('\033[31mVocê não pode usar o menu aqui.\033[m')
								sleep(2)
								uteis.clear()
							if res == 1:
								title('\033[31mEstá trancada.\033[m')
								sleep(2)
								uteis.clear()
							elif res == 3:
								if sod == 'False':
									title('\033[31mEstá trancada...\033[m')
									sleep(2)
									uteis.clear()
								else:
									title('\033[34mLá dentro tem um diário.\033[m')
									sleep(2)
									tsave()
							elif res == 2:
								if sod == 'False':
									title('\033[34mEsta é a sala do trono, nele você vê o rei e aquele soldado.\033[m')
									sleep(2)
									title('\033[34mO soldado e o rei estão discutindo sobre uma tal esfera "magica".\033[m')
									sleep(2)
									title('\033[34mDe repente eles notam sua presença, o soldado reconhece você.\033[m')
									sleep(2)
									title('\033[32mSoldado: Ainda bem que você chegou!\033[m')
									sleep(2)
									title('\033[32mSoldado: Eu vi quando você derrotou o ladrão.\033[m')
									sleep(2)
									uteis.clear()
									title('\033[32mSoldado: Não me pergunte como.\033[m')
									sleep(2)
									title('\033[33mRei: Eu estou feliz que alquem podê ajudar.\033[m')
									sleep(2)
									title('\033[33mRei: Acontece que aquele não era um simples ladrão.\033[m')
									sleep(2)
									title('\033[33mRei: Ele era um dos mais poderosos magos da história.\033[m')
									sleep(2)
									title('\033[33mRei: E já que você o derrotou, eu quero que você nos ajude em uma missão.\033[m')
									sleep(2)
									title('\033[33mRei: Quero que você recupere o Orb do poder.\033[m')
									sleep(2)
									uteis.clear()
									title('\033[32mSoldado: Você aceita?\033[m')
									sleep(2)
									print('[ 1 ] Sim\n[ 2 ] Não')
									res = uteis.inint('Sua escolha: ')
									uteis.clear()
									if res == 1:
										title('\033[33mRei: Certo, o soldado irá acompanha-lo.\033[m')
										sleep(2)
										sod = 'True'
										title('\033[32mSoldado: Eu te esperarei na minha casa.\033[m')
										sleep(2)
									elif res == 2:
										title('\033[33mRei: Ok, você pode voltar para casa.\033[m')
										sleep(2)
										print('\033[31mGamer over.\033[m')
										sleep(2)
										gameover = 'True'
							elif res == 4:
								title('\033[33mVolte sempre.\033[m')
								sleep(2)
								uteis.clear()
								break
			else:
				erro()
#------------------------ ESTÁGIO 4 (EM CONSTRUÇÃO) ----------------------------
		while True:
			city = 'Mililand'
			if gameover == 'True':
				break
			if stage4 == 'False':
				break
			while True:
				if gameover == 'True':
					break
				if stage4 == 'False':
					break
				title('\033[34mMililand, a "cidade dos sonhos".\033[m')
				sleep(2)
				title('\033[34mDe acordo com Bart, essa cidade é a mais populosa da região.\033[m')
				sleep(2)
				title('\033[34mHá muitos lugares para ir.\033[m')
				sleep(2)
				print('[ 1 ] Hospedaria  [ 4 ] Moinho\n[ 2 ] Casa 1      [ 5 ] Casa 2\n[ 3 ] Loja        [ 6 ] Casa 3')
				res = uteis.inint('Sua escolha: ')
				uteis.clear()
				if res == 999:
					menuj()
				else:
					print('sorry, but this game is just a demo.')
					print('The game "Fantasy Empires" will only be \nfinished when technical errors are corrected.')
					for c in range(1,13):
						print('\033[1;33m...', end='', flush=True)
						sleep(1)
					gameover = 'True'
