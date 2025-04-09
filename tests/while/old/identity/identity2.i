L1:	i = 0
L3:L5:	j = 0
L6:L8:	t1 = i * 80
	t2 = j * 8
	t3 = t1 + t2
	a [ t3 ] = 0.0
L9:	j = j + 1
L10:	iffalse j >= 10 goto L6
L11:	goto L7
	goto L6
L7:	i = i + 1
L12:	iffalse i >= 10 goto L3
L13:	goto L4
	goto L3
L4:	i = 0
L14:L15:	t4 = i * 80
	t5 = i * 8
	t6 = t4 + t5
	a [ t6 ] = 1.0
L16:	i = i + 1
L17:	iffalse i >= 10 goto L14
L18:	goto L2
	goto L14
L2:
