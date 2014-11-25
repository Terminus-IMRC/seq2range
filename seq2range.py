#!/usr/bin/env python3
n_prev=None
continuous=False

while True:
	try:
		s=input()
	except EOFError:
		break
	
	n=int(s)
	if n_prev==None:
		print("%d"%(n), end="")
	elif n!=n_prev and n-1!=n_prev:
		if continuous:
			print("-%d,%d"%(n_prev, n), end="")
		else:
			print(",%d"%(n), end="")
		continuous=False
	else:
		continuous=True
	
	n_prev=n

if continuous:
	print("-%d"%(n))
else:
	print("")
