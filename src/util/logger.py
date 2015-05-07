V = VERBOSE = 2
I = INFO = 1
E = ERROR = 0

LVL = I

def log(lvl, msg):
	if lvl <= LVL:
		print(msg)