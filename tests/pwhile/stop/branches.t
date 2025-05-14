{
    	int a; int x; bool y; float z;
	
    a = 1;
	x = 0;
	y = true;
    z = 4.4;

    if (a < x) {
        a = x + 1;
	    stop;
    } else {
        x = a;
    }

    choose {
        1: {
            stop;
        }
        2: {
            a = x;
            stop;
        }
        1: {
            
        }
    }

	x = 1;
	y = false;
	z = 5.1;
}