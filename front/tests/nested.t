{
	int r; int dd; int a; int d;
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
        do {
            prod = prod + a[i]*b[i];
            i = i+1;
        } while (i <= 20);
    }

}
