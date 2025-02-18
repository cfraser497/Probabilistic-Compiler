L1:	r = a
L3:	dd = d
L4:	iffalse dd <= r goto L5
L6:	dd = 2 * dd
	goto L4
L5:	iffalse dd != r goto L7
L8:	dd = dd / 2
L9:	iffalse dd <= r goto L5
L10:	r = r - dd
	goto L5
L7:	prod = 0
L11:	i = 1
L12:	t1 = i * 8
	t2 = a [ t1 ]
	t3 = i * 8
	t4 = b [ t3 ]
	t5 = t2 * t4
	prod = prod + t5
L14:	i = i + 1
L13:	if i <= 20 goto L12
L2:
