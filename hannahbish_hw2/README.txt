(d) My "back of the envelope" estimate gives beta_0 = 0.72 and beta_1 = 0.96, but since this is not a precise method of caclculation the results vary greatly between runs.
(f) My gridsearch.py program givesbeta_0 = 1.61 and beta_1 = 2.97




To run logistic regression program:

1. Run makedata.py. This will produce a file 'data.out' containing the generated x and y pairs.
If necessary the variables N, beta_0, beta_1, and L can be adjusted at the top of the code.
Makedata.py outputs two plots: one, 'yvsx.png', shows the full set of x,y pairs, and the other 'yvsx_zoom.png', shows the same data zoomed in on the region near x_0.
Running this code will also output "back of the envelope" results.

2. Run gridsearch.py. This will read in x,y pairs output to data.txt by makedata.py.
If necessary the number of grid values for each parameter, ngridvals, can be adjusted at the top of the code.
Running this code will output the maximum likelihood values of beta_0 and beta_1.
