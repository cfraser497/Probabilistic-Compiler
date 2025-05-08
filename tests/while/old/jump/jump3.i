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
L6:	t1 = i * 1
	a [ t1 ] = false
L7:	r = b
L8:	t2 = i * 1
	r = a [ t2 ]
L9:	t3 = i * 1
	a [ t3 ] = b
L10:	t4 = i * 1
	a [ t4 ] = true
L11:	t5 = i * 1
	a [ t5 ] = false
L12:	iffalse b goto L13
L14:	x = y
L13:	t6 = i * 1
	t7 = a [ t6 ]
	iffalse t7 goto L2
L15:	x = y
L2:	stop
