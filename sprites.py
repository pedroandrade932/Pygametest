#from uteis import end
def aranha(cora='\033[41m', coro='\033[40m'):
	print('--'*15)
	print(f'\033[1;37m               |         \033[m')
	print(f'\033[1;37m               |         \033[m')
	print(f'            {cora}       \033[m')
	print(f'          {cora}           \033[m')
	print(f'       {cora}  \033[m{cora}             \033[m{cora}   \033[m')
	print(f'      {cora}  \033[m  {cora}   {coro} \033[m{cora}   {coro} \033[m{cora}   \033[m  {cora}   \033[m')
	print(f'     {cora}  \033[m    {cora}         \033[m     {cora}  \033[m')
	print(f'            {cora}  \033[m   {cora}  \033[m')
	print('--'*15)


def ladrao():
	corc = '\033[44m'
	coro = '\033[41m'
	nill = '\033[m'
	print('--'*15)
	print(f'        {corc}       {nill}')
	print(f'       {corc}  {nill}      {corc} {nill}')
	print(f'       {corc}  {nill} {coro} {nill}  {coro} {nill} {corc} {nill}')
	print(f'       {corc}  {nill}     {corc} {nill}')
	print(f'       {corc}  {nill}    {corc} {nill}')
	print('--'*15)


#aranha()
#ladrao()
#end()
