{
	int a; int b; a = 0; b = 0;
	{
        if (a < b) {
            a = a + 1;
            b = b + 1;
            b = b + a;
        }
        else {
            a = a + 2;
            b = b + 2;
            a = a + b;
        }
	}
	a = a + 1; b = b + 1;
}
