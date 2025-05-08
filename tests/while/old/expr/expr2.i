.data:
  a : int { -10 .. 10 }
  b : int { -10 .. 10 }
  c : int { -10 .. 10 }
  d : int { -10 .. 10 }
  term : float
.code:
L1:	a = 1
L3:	b = 2
L4:	c = 3
L5:	d = 4
L6:	term = 5.0
L7:	a = b + c
L8:	a = b - c
L9:	a = b * c
L10:	a = b / c
L11:	a = - b
L12:	a = 1
L13:	t1 = a - b
	d = t1 - c
L14:	t2 = a * b
	d = t2 * c
L15:	t3 = b * c
	d = a + t3
L16:	t4 = a * b
	d = t4 + c
L17:	t5 = a - b
	d = t5 - c
L18:	t6 = b - c
	d = a - t6
L19:	t7 = a + b
	d = t7 * c
L20:	t8 = b + c
	d = a * t8
L21:	t9 = b * b
	t10 = 4.0 * a
	t11 = t10 * c
	term = t9 - t11
L2:	stop
