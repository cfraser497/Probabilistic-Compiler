{
        int x; int y; int z;
	
	x = 0;
	y = 1;

	choose {
		1: {
            x = 0;
            y = x;
            z = 1;
        }
		2: {
            y = 1;
            x = y;
            z = 2;
        }
	}
}