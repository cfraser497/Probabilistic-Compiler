.data:
  a : int { -10 .. 10 }
  b : bool
  c : int { -10 .. 10 }
  d : int { -10 .. 10 }
.code:
L1:	a = 1
L3:	b = true
L4:	c = 3
L5:	d = 4
L6:	b = ((a + 1 > d - c) || true)
L2:	stop
