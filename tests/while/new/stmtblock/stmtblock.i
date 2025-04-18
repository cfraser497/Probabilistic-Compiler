.data:
  a: int{-10..10}
  b: int{-10..10}
  b: int{-10..10}
  a: int{-10..10}
  b: int{-10..10}
.code:
L1:	a = 0
L3:	b = 0
L4:	b = 1
L6:	a = 2
L7:	b = 3
L8:	iffalse a < b goto L9
L10:	a = a + 1
L11:	b = b + 1
L12:	b = b + a
L9:	iffalse a < b goto L5
L13:	a = a + 2
L14:	b = b + 2
L15:	a = a + b
	goto L9
L5:	a = a + 1
L16:	b = b + 1
L2:
