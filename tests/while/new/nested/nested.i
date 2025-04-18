.data:
  r: int{-10..10}
  dd: int{-10..10}
  a: int{-10..10}
  d: int{-10..10}
  i: int{-10..10}
  prod: float
  a: [20] float
  b: [20] float
.code:
L1:	a = 50
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
L14:	iffalse i < 20 goto L15
L16:	t1 = i * 8
	a [ t1 ] = 2.0
L17:	t2 = i * 8
	b [ t2 ] = 3.0
L18:	i = i + 1
	goto L14
L15:	i = 1
L19:	t3 = i * 8
	t4 = a [ t3 ]
	t5 = i * 8
	t6 = b [ t5 ]
	t7 = t4 * t6
	prod = prod + t7
L21:	i = i + 1
L20:	if i <= 20 goto L19
L2:
