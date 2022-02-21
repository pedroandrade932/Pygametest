def nill():
	return '\033[m'

def white(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};37m'
	else:
		typ == 0


def red(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};31m'
	else:
		typ == 0


def green(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};32m'
	else:
		typ == 0


def yellow(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};33m'
	else:
		typ == 0


def blue(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};34m'
	else:
		typ == 0


def purple(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};35m'
	else:
		typ == 0


def cyan(typ=0):
	typ = str(typ)
	if typ.isnumeric():
		return f'\033[{typ};36m'
	else:
		typ == 0

