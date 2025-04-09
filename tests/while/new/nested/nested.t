{
	int r; int dd; int a; int d;

	a = 50;
	d = 5;

	r = a; dd = d;
	while( dd <= r ) dd = 2*dd;
	while( dd != r ) {
		dd = dd/2;
		if (dd <= r) r = r - dd;
	}

    {
        int i; float prod; float [20] a; float [20] b;
      	prod = 0;
        i = 1;

        while ( i < 20 ) {
            a[i] = 2.0;
            b[i] = 3.0;
            i = i + 1;
        }

        i = 1;
        do {
            prod = prod + a[i]*b[i];
            i = i+1;
        } while (i <= 20);
    }

}
