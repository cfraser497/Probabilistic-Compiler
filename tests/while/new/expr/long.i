.data:
  a : int { -10 .. 10 }
  b : int { -10 .. 10 }
  c : int { -10 .. 10 }
  d : int { -10 .. 10 }
.code:
L1:	a = 1
L3:	b = 2
L4:	c = 3
L5:	d = 4
L6:	d = a - b * c
L7:	d = a - b - (c + d - 4 + 1) * d + 10
L2:	stop
