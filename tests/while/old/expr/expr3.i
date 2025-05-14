.data:
  x : int { -10 .. 10 }
  y : int { -10 .. 10 }
  r : bool
.code:
L1:	x = 1
L3:	y = 2
L4:	r = ! (x < y)
L5:	r = ! ! (x == y)
L6:	if x > y goto L9
L8:	r = true
	goto L7
L9:	r = false
L7:	iffalse x != y goto L11
L10:	r = true
	goto L2
L11:	r = false
L2:	stop
