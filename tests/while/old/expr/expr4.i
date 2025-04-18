10
.data:
  i: int{-10..10}
  j: int{-10..10}
  k: int{-10..10}
  a: int{-10..10}
  x: int{-10..10}
  c: int{-10..10}
  b: [10] [10] [10] bool
  d: bool
.code:
L1:	i = 1
L3:	j = 2
L4:	k = 3
L5:	c = 4
L6:	t1 = i * 12
	t2 = j * 4
	t3 = t1 + t2
	a [ t3 ] = 0
L7:	t4 = i * 12
	t5 = j * 4
	t6 = t4 + t5
	t7 = a [ t6 ]
	x = c + t7
L8:	t8 = i * 100
	t9 = j * 10
	t10 = t8 + t9
	t11 = k * 1
	t12 = t10 + t11
	b [ t12 ] = true
L9:	t13 = i * 100
	t14 = j * 10
	t15 = t13 + t14
	t16 = k * 1
	t17 = t15 + t16
	d = b [ t17 ]
L2:
