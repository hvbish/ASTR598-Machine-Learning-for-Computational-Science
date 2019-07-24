(f) The homoscedatic residuals do not show any correlation with x. They are always normally distributed about the given mu, with standard deviation of the given sigma.
(k) The heteroscedastic residuals do show a pattern with x. Since the noise goes as cx, the variance of the residuals goes as x^2.



To run linear regression program:

1. Run makedata.py. This will produce a file 'data.out' as described in part (c)
2. Run makedata2.py. This will produce a file 'data2.out' as described in part (h)
3. Run fitdata.py. This will perform least squares regression on the data in the .out files, and produce plots showing the least squares fit ('homofit.png','heterofit.png') and residuals ('homoresiduals.png','heteroresiduals.png') for both.