L1:	x = 0
L3:	y = 1
L4:	flip 1/5 goto L5 2/5 goto L6 2/5 goto L7
L5:	x = y
	goto L2
L6:	y = x
	goto L2
L7:	y = y + 1
L2:
