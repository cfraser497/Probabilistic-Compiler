{
	int BLANK; int TAB; int NEWLINE; int peek; int line; int readch;
	readch = 4;	

	while( true ) {
		if( peek == BLANK || peek == TAB ) ;
		else if( peek == NEWLINE ) line = line + 1;
		else break;
		peek = readch;
		break;
	}
}
