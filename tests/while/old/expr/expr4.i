.data:
  i : int { -10 .. 10 }
  j : int { -10 .. 10 }
  k : int { -10 .. 10 }
  a : [2] [3] int { -10 .. 10 }
  x : int { -10 .. 10 }
  c : int { -10 .. 10 }
  b : [10] [10] [10] bool
  d : bool
.code:
L1:	i = 1
L3:	j = 2
L4:	k = 3
L5:	c = 4
L6:	a [ i * 12 + j * 4 ] = 0
L7:	t1 = a [ i * 12 + j * 4 ]
	x = c + t1
L8:	b [ i * 100 + j * 10 + k * 1 ] = true
L9:	d = b [ i * 100 + j * 10 + k * 1 ]
L2:	stop
