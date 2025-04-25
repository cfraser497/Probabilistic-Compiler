.data:
  BLANK : int { -10 .. 10 }
  TAB : int { -10 .. 10 }
  NEWLINE : int { -10 .. 10 }
  peek : int { -10 .. 10 }
  line : int { -10 .. 10 }
  readch : int { -10 .. 10 }
.code:
L1:	readch = 4
L3:L4:	if peek == BLANK goto L8
	iffalse peek == TAB goto L7
L8:L6:	goto L5
L7:	iffalse peek == NEWLINE goto L10
L9:	line = line + 1
	goto L5
L10:	goto L2
L5:	peek = readch
L11:	goto L2
	goto L3
L2:
