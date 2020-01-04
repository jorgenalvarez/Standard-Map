#include <stdio.h>
#include <math.h>

double MU;

void standard_map (double t, double x[], double f[])
{
	f[1] = x[1] - MU*sin(x[0]);
	f[0] = x[0] + f[1];
}
