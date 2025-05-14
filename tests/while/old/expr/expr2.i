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
L13:	d = a - b - c
L14:	d = a * b * c
L15:	d = a + b * c
L16:	d = a * b + c
L17:	d = a - b - c
L18:	d = a - b - c
L19:	d = a + b * c
L20:	d = a * b + c
L21:	term = b * b - 4.0 * a * c
L2:	stop
