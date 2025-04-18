.data:
  a: int{-10..10}
  b: int{-10..10}
.code:
L1:	a = 0
L3:	b = 0
L4:	iffalse a < b goto L5
L6:L5:	a = a + 1
L7:	b = b + 1
L2:
