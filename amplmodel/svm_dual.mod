#MODEL PARAMETERS

# number of points
param n;
# number of dimensions of each point
param m;

# points
param x{i in 1..n, j in 1..m};

# label of each point
param y{i in 1..n};

# nu
param nu;

# VARIABLE
var lambda {i in 1..n};
var w{i in 1..m};
var gamma;

# target

maximize obj_func : 
	sum{i in 1..n} lambda[i] -
	0.5*sum{i in 1..n, j in 1..n} lambda[i]*lambda[j]*y[i]*y[j]*
	(sum{k in 1..m}x[i,k]*x[j,k]);

# constraints

subject to constraint: 
	sum{i in 1..n}lambda[i]*y[i]=0;
	
subject to lam1{i in 1..n}: 
	lambda[i]>=0;
	
subject to lam2{i in 1..n}:
	lambda[i]<=nu;
	
subject to get_w{i in 1..m}:
	 w[i]=sum{j in 1..n}lambda[j]*y[j]*x[j,i];

#subject to get_gamma:
	#gamma=sum{i in 1..n}(1/(y[i]) - sum{j in 1..m}( w[j] *x[i,j])) ;
	
