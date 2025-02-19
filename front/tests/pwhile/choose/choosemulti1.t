{
        int x; int y;
	
	x = 0;
	y = 1;

	choose {
		1: x = y;
		2: y = x;
        2: y = y + 1;
	}
}