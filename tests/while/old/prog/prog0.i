10
.data:
  temp: int{-10..10}
  i: int{-10..10}
  j: int{-10..10}
  v: float
  x: float
  a: [100] float
.code:
L1:	i = 0
L3:	j = 100
L4:	v = 50.0
L5:	temp = 1.0
L6:	iffalse i < j goto L7
L8:	t1 = i * 8
	a [ t1 ] = temp
L9:	temp = temp + 1.0
L10:	i = i + 1
	goto L6
L7:	i = - 1
L11:L12:	i = i + 1
L14:	t2 = i * 8
	t3 = a [ t2 ]
	if t3 < v goto L12
L13:	j = j - 1
L16:	t4 = j * 8
	t5 = a [ t4 ]
	if t5 > v goto L13
L15:	iffalse i >= j goto L17
L18:	goto L2
L17:	t6 = i * 8
	x = a [ t6 ]
L19:	t7 = i * 8
	t8 = j * 8
	t9 = a [ t8 ]
	a [ t7 ] = t9
L20:	t10 = j * 8
	a [ t10 ] = x
	goto L11
L2:
