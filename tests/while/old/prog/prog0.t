{
	int temp; int i; int j; int v; int x; int[100] a;

	i = 0;
	j = 5;
	v = 0;

	temp = 1;

	while ( i < j ) {
		a[i] = temp;
		temp = temp + 1;
		i = i + 1;
	}

	i = -1;

	while( true ) {
		do i = i+1; while( a[i] < v);
		do j = j-1; while( a[j] > v);
		if( i >= j ) break;
		x = a[i]; a[i] = a[j]; a[j] = x;
	}
}
