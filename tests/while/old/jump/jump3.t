{
        bool b; bool r; bool[11] a; int i; int x; int y;

	b = true;
	i = 0;
	x = 1;
	y = 2;
	a[i] = false;

	r = b;

	r = a[i];

	a[i] = b;

	a[i] = true;

	a[i] = false;

	if( b ) x = y;

	if( a[i] ) x = y;

}
