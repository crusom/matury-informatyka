double szukajMiejscaZerowego(wielomian* w, double a, double b, double p = 0.0000001) {
  double fa = wartosc_wielomianu(w, a);
  if (fa == 0) return a;
  double fb = wartosc_wielomianu(w, b);
  if (fb == 0) return b;
  if (fa * fb > 0)
	return NULL;
  double c, fc;
  do {
	c = (a + b) / 2;
	fc = wartosc_wielomianu(w, c);
	if (fc == 0) return c;
	if (fc * fa > 0) {
	  a = c;
	  fa = fc;
	} else {
	  b = c;
	  fb = fc;
	}
  } while (abs(fc) > p);
  return c;
}


