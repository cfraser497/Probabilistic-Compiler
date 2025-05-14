.data:
  r : int { -10 .. 10 }
  dd : int { -10 .. 10 }
  a : int { -10 .. 10 }
  d : int { -10 .. 10 }
  i : int { -10 .. 10 }
  prod : int { -10 .. 10 }
  b : [20] int { -10 .. 10 }
.code:
L1:	a = 5
L3:	d = 5
L4:	r = a
L5:	dd = d
L6:	iffalse dd <= r goto L7
L8:	dd = 2 * dd
	goto L6
L7:	iffalse dd != r goto L9
L10:	dd = dd / 2
L11:	iffalse dd <= r goto L7
L12:	r = r - dd
	goto L7
L9:	prod = 0
L13:	i = 1
L14:	iffalse i < 9 goto L15
L16:	a [ i * 4 ] = 2
L17:	b [ i * 4 ] = 1
L18:	i = i + 1
	goto L14
L15:	i = 1
L19:	prod = prod + a [ i * 4 ] * b [ i * 4 ]
L21:	i = i + 1
L20:	if i <= 2 goto L19
L2:	stop
