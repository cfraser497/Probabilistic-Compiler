.data:
  a : int { -10 .. 10 }
  x : int { -10 .. 10 }
  y : bool
  z : float
.code:
L1:	a = 1
L3:	x = 0
L4:	y = true
L5:	z = 4.4
L6:	iffalse a < x goto L9
L8:	a = x + 1
L10:	stop
	goto L7
L9:	x = a
L7:	flip 1 goto L12 2 goto L13 1 goto L14
L12:	stop
	goto L11
L13:	a = x
L15:	stop
	goto L11
L14:L11:	x = 1
L16:	y = false
L17:	z = 5.1
L2:	stop
