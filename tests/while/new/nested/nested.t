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

    {
        int i; int prod; int [20] a; int [20] b;
      	prod = 0;
        i = 1;

        while ( i < 9 ) {
            a[i] = 2;
            b[i] = 1;
            i = i + 1;
        }

        i = 1;
        do {
            prod = prod + a[i]*b[i];
            i = i+1;
        } while (i <= 2);
    }

}
