10
.data:
  BLANK: int{-10..10}
  TAB: int{-10..10}
  NEWLINE: int{-10..10}
  peek: int{-10..10}
  line: int{-10..10}
  readch: int{-10..10}
.code:
L1:L3:	if peek == BLANK goto L7
	iffalse peek == TAB goto L6
L7:L5:	goto L4
L6:	iffalse peek == NEWLINE goto L9
L8:	line = line + 1
	goto L4
L9:	goto L2
L4:	peek = readch
L10:	goto L2
	goto L1
L2:
