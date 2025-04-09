{
        int x; int y; bool r;

		x = 1;
		y = 2;

        r = !(x < y);

	r = !!(x == y);

	if( !(x > y) ) r = true;
	else r = false;

	if( !!(x != y) ) r = true;
	else r = false;

}
