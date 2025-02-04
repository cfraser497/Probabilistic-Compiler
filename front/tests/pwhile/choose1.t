{
        bool b; bool r; bool[11] a; int i; int x; int y;

	r = b;

	r = a[i];

	a[i] = b;

	a[i] = true;

	a[i] = false;

	choose( 1 ) x = y;

	( 2 ) x = y;

}


choose {
	1: {

	}
	2: {

	}
	1: {

	}
}

choose {
	(1) {

	}
	(2) {

	}
	(1) {

	}
}

choose {
	(1) x = y;
	(2) y = x;
	(1) y = y + 1;
}