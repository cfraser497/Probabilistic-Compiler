{
	int r; int dd; int a; int d;

	a = 5;
	d = 5;
	
	r = a; dd = d;
	while( dd <= r ) dd = 2*dd;
	while( dd != r ) {
		dd = dd/2;
		if (dd <= r) r = r - dd;
	}
}
