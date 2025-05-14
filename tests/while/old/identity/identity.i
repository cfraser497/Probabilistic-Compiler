.data:
  i : int { -10 .. 10 }
  j : int { -10 .. 10 }
  a : [10] [10] float
.code:
L1:	i = 0
L3:	iffalse i < 10 goto L4
L5:	j = 0
L6:	iffalse j < 10 goto L7
L8:	a [ i * 80 + j * 8 ] = 0.0
L9:	j = j + 1
	goto L6
L7:	i = i + 1
	goto L3
L4:	i = 0
L10:	iffalse i < 10 goto L2
L11:	a [ i * 80 + i * 8 ] = 1.0
L12:	i = i + 1
	goto L10
L2:	stop
