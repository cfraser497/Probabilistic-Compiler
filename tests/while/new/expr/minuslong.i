.data:
  a : int { -10 .. 10 }
  b : int { -10 .. 10 }
  c : int { -10 .. 10 }
  d : int { -10 .. 10 }
.code:
L1:	a = 4
L3:	b = 2
L4:	c = 3
L5:	d = 1
L6:	d = - a + b - c * d
L2:	stop
