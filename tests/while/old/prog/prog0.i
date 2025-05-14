.data:
  temp : int { -10 .. 10 }
  i : int { -10 .. 10 }
  j : int { -10 .. 10 }
  v : int { -10 .. 10 }
  x : int { -10 .. 10 }
  a : [100] int { -10 .. 10 }
.code:
L1:	i = 0
L3:	j = 5
L4:	v = 0
L5:	temp = 1
L6:	iffalse i < j goto L7
L8:	a [ i * 4 ] = temp
L9:	temp = temp + 1
L10:	i = i + 1
	goto L6
L7:	i = - 1
L11:L12:	i = i + 1
L14:	if a [ i * 4 ] < v goto L12
L13:	j = j - 1
L16:	if a [ j * 4 ] > v goto L13
L15:	iffalse i >= j goto L17
L18:	goto L2
L17:	x = a [ i * 4 ]
L19:	a [ i * 4 ] = a [ j * 4 ]
L20:	a [ j * 4 ] = x
	goto L11
L2:	stop
