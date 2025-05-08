.data:
  x : int { -10 .. 10 }
  y : int { -10 .. 10 }
  a : int { -10 .. 10 }
  b : int { -10 .. 10 }
  r : bool
.code:
L1:	x = 1
L3:	y = 2
L4:	a = 3
L5:	b = 4
L6:	r = true
L7:	r = false
L8:	iffalse a < b goto L10
	t1 = true
	goto L11
L10:	t1 = false
L11:	r = t1
L9:	iffalse x <= y goto L13
	t2 = true
	goto L14
L13:	t2 = false
L14:	r = t2
L12:	iffalse a == b goto L16
	t3 = true
	goto L17
L16:	t3 = false
L17:	r = t3
L15:	iffalse x != y goto L19
	t4 = true
	goto L20
L19:	t4 = false
L20:	r = t4
L18:	iffalse a >= b goto L22
	t5 = true
	goto L23
L22:	t5 = false
L23:	r = t5
L21:	iffalse x > y goto L25
	t6 = true
	goto L26
L25:	t6 = false
L26:	r = t6
L24:	if x < 100 goto L30
	iffalse x > 200 goto L28
L30:	t7 = true
	goto L29
L28:	t7 = false
L29:	r = t7
L27:	iffalse a < 100 goto L32
	iffalse a > 200 goto L32
	t8 = true
	goto L33
L32:	t8 = false
L33:	r = t8
L31:	if x < 100 goto L37
	iffalse x > 200 goto L35
	iffalse x != y goto L35
L37:	t9 = true
	goto L36
L35:	t9 = false
L36:	r = t9
L34:	if a < 100 goto L41
	iffalse a > 200 goto L42
	if a != 150 goto L41
L42:	iffalse a != 0 goto L39
L41:	t10 = true
	goto L40
L39:	t10 = false
L40:	r = t10
L38:	iffalse x > 200 goto L47
	if x != b goto L46
L47:	iffalse x < 100 goto L44
L46:	t11 = true
	goto L45
L44:	t11 = false
L45:	r = t11
L43:	if a < 100 goto L50
	iffalse a > 200 goto L48
	iffalse a != b goto L48
L50:	t12 = true
	goto L49
L48:	t12 = false
L49:	r = t12
L2:	stop
