{
	int temp; int i; int j; float v; float x; float[100] a;

	i = 0;
	j = 100;
	v = 50.0;

	temp = 1.0;

	while ( i < j ) {
		a[i] = temp;
		temp = temp + 1.0;
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
