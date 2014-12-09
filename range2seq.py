#!/usr/bin/env python3
s=input()

t=''
hflag=False
for x in s:
	if x==',':
		if hflag:
			for y in range(int(t_start), int(t)+1):
				print(y)
			hflag=False
		else:
			print(t)
		t=''
	elif x=='-':
		hflag=True
		t_start=t
		t=''
	else:
		t+=x
if hflag:
	for y in range(int(t_start), int(t)+1):
		print(y)
else:
	print(t)
