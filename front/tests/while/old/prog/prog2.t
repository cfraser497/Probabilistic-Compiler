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
