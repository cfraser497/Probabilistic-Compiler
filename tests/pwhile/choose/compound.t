{
        int x; int y; int z;
	
	x = 0;
	y = 1;

	choose {
		1: {
            x = 0;
            y = x;
            z = 1*x+1-0;
        }
		2: {
            y = 1;
            x = y;
            z = 5+2*x+4-4;
        }
	}
}