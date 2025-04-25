.data:
  x : int { -10 .. 10 }
  y : int { -10 .. 10 }
.code:
L1:	x = 0
L3:	y = 1
L4:	flip 1 goto L6 2 goto L7
L6:	x = 0
	goto L5
L7:	y = 1
L5:	x = y
L8:	y = x
L2:
