10
.data:
  r: int{-10..10}
  dd: int{-10..10}
  a: int{-10..10}
  d: int{-10..10}
.code:
L1:	a = 50
L3:	d = 5
L4:	r = a
L5:	dd = d
L6:	iffalse dd <= r goto L7
L8:	dd = 2 * dd
	goto L6
L7:	iffalse dd != r goto L2
L9:	dd = dd / 2
L10:	iffalse dd <= r goto L7
L11:	r = r - dd
	goto L7
L2:
