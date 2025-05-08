.data:
  x : int { -10 .. 10 }
  y : int { -10 .. 10 }
.code:
L1:	x = 0
L3:	y = 1
L4:	flip 1 goto L5 2 goto L6
L5:	x = 0
	goto L2
L6:	y = 1
L2:	stop
