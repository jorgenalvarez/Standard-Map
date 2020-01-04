#include <stdio.h>
#include <math.h>

double MU;

void standard_map (double x[])
{
	x[1] = x[1] - MU*sin(x[0]);
	x[0] = x[0] + x[1];
}
