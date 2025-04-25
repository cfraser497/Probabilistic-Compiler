{
	int i; int prod; int [20] a; int [20] b;
	prod = 0;
	i = 1;

	while ( i < 5 ) {
		a[i] = 1;
		b[i] = 2;
		i = i + 1;
	}

	i = 1;

	do {
		prod = prod + a[i]*b[i];
		i = i+1;
	} while (i <= 2);
}
