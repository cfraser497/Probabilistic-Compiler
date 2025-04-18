10
.data:
  a: int{-10..10}
  b: int{-10..10}
  c: int{-10..10}
  d: int{-10..10}
.code:
L1:	a = 1
L3:	b = 2
L4:	c = 3
L5:	d = 4
L6:	t1 = a - b
	t2 = d - 4
	t3 = c + t2
	t4 = t3 + 1.3
	t5 = t4 * d
	d = t1 - t5
L2:
