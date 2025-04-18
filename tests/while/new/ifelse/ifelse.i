.data:
  a: int{-10..10}
  b: int{-10..10}
.code:
L1:	a = 0
L3:	b = 0
L4:	iffalse a < b goto L7
L6:	a = a + 1
L8:	b = b + 1
L9:	b = b + a
	goto L5
L7:	a = a + 2
L10:	b = b + 2
L11:	a = a + b
L5:	a = a + 1
L12:	b = b + 1
L2:
