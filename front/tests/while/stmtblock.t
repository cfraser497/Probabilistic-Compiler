{
	int a; int b; a = 0; b = 0;
	{
		int b; b = 1;
		{
			int a; a = 2;
		}
		{
			int b; b = 3;
		}
        if (a < b) {
            a = a + 1;
            b = b + 1;
            b = b + a;
        }

        while (a < b) {
            a = a + 2;
            b = b + 2;
            a = a + b;
        }
	}
	a = a + 1; b = b + 1;
}
