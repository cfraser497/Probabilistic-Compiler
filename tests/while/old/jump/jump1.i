.data:
  x: int{-10..10}
  y: int{-10..10}
  a: int{-10..10}
  b: int{-10..10}
.code:
L1:	x = 1
L3:	y = 2
L4:	a = 3
L5:	b = 4
L6:L8:	a = 0
L7:	goto L9
L10:	x = 0
L9:	iffalse a < b goto L11
L12:	a = b
L11:	iffalse x <= y goto L13
L14:	x = y
L13:	iffalse a == b goto L15
L16:	a = b
L15:	iffalse x != y goto L17
L18:	x = y
L17:	iffalse a >= b goto L19
L20:	b = a
L19:	iffalse x > y goto L21
L22:	y = x
L21:	iffalse a == b goto L23
L24:L23:	if x < 100 goto L27
	iffalse x > 200 goto L25
L27:L26:	x = 0
L25:	iffalse a < 100 goto L28
	iffalse a > 200 goto L28
L29:	b = 0
L28:	if x < 100 goto L32
	iffalse x > 200 goto L30
	iffalse x != y goto L30
L32:L31:	x = 0
L30:	if a < 100 goto L35
	iffalse a > 200 goto L36
	if a != 150 goto L35
L36:	iffalse a != 0 goto L33
L35:L34:	a = 0
L33:	iffalse x > 200 goto L40
	if x != b goto L39
L40:	iffalse x < 100 goto L37
L39:L38:	x = 0
L37:	if a < 100 goto L42
	iffalse a > 200 goto L2
	iffalse a != b goto L2
L42:L41:	a = 0
L2:
