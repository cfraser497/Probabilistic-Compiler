.data:
  i : int { -10 .. 10 }
  prod : int { -10 .. 10 }
  a : [20] int { -10 .. 10 }
  b : [20] int { -10 .. 10 }
.code:
L1:	prod = 0
L3:	i = 1
L4:	iffalse i < 5 goto L5
L6:	t1 = i * 4
	a [ t1 ] = 1
L7:	t2 = i * 4
	b [ t2 ] = 2
L8:	i = i + 1
	goto L4
L5:	i = 1
L9:	t3 = i * 4
	t4 = a [ t3 ]
	t5 = i * 4
	t6 = b [ t5 ]
	t7 = t4 * t6
	prod = prod + t7
L11:	i = i + 1
L10:	if i <= 2 goto L9
L2:
