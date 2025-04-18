.data:
  x: int{-10..10}
  y: int{-10..10}
  r: bool
.code:
L1:	x = 1
L3:	y = 2
L4:	if x < y goto L6
	t1 = true
	goto L7
L6:	t1 = false
L7:	r = t1
L5:	iffalse x == y goto L9
	t2 = true
	goto L10
L9:	t2 = false
L10:	r = t2
L8:	if x > y goto L13
L12:	r = true
	goto L11
L13:	r = false
L11:	iffalse x != y goto L15
L14:	r = true
	goto L2
L15:	r = false
L2:
