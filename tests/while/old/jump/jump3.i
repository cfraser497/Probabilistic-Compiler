.data:
  b : bool
  r : bool
  a : [11] bool
  i : int { -10 .. 10 }
  x : int { -10 .. 10 }
  y : int { -10 .. 10 }
.code:
L1:	b = true
L3:	i = 0
L4:	x = 1
L5:	y = 2
L6:	a [ i * 1 ] = false
L7:	r = b
L8:	r = a [ i * 1 ]
L9:	a [ i * 1 ] = b
L10:	a [ i * 1 ] = true
L11:	a [ i * 1 ] = false
L12:	iffalse b goto L13
L14:	x = y
L13:	t1 = a [ i * 1 ]
	iffalse t1 goto L2
L15:	x = y
L2:	stop
