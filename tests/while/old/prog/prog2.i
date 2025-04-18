10
.data:
  i: int{-10..10}
  prod: float
  a: [20] float
  b: [20] float
.code:
L1:	prod = 0
L3:	i = 1
L4:	iffalse i < 20 goto L5
L6:	t1 = i * 8
	a [ t1 ] = 2.0
L7:	t2 = i * 8
	b [ t2 ] = 3.0
L8:	i = i + 1
	goto L4
L5:	i = 1
L9:	t3 = i * 8
	t4 = a [ t3 ]
	t5 = i * 8
	t6 = b [ t5 ]
	t7 = t4 * t6
	prod = prod + t7
L11:	i = i + 1
L10:	if i <= 20 goto L9
L2:
