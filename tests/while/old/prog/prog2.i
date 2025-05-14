.data:
  i : int { -10 .. 10 }
  prod : int { -10 .. 10 }
  a : [20] int { -10 .. 10 }
  b : [20] int { -10 .. 10 }
.code:
L1:	prod = 0
L3:	i = 1
L4:	iffalse i < 5 goto L5
L6:	a [ i * 4 ] = 1
L7:	b [ i * 4 ] = 2
L8:	i = i + 1
	goto L4
L5:	i = 1
L9:	prod = prod + a [ i * 4 ] * b [ i * 4 ]
L11:	i = i + 1
L10:	if i <= 2 goto L9
L2:	stop
