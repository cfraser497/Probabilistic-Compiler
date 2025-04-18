10
.data:
  a: bool
  b: bool
.code:
L1:	a = true
L3:	b = false
L4:	if b goto L5
	t1 = true
	goto L6
L5:	t1 = false
L6:	a = t1
L2:
