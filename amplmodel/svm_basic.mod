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

#VARIABLES

var w{i in 1..m};
# intercept 
var gamma;
# slack 
var s{i in 1..n};


# OBJECTIVE FUNCTION
minimize target: 
	0.5*sum{i in 1..m} (w[i]^2) + nu*sum{i in 1..n}s[i];

# CONSTRAINTS
subject to main{i in 1..n}:
	y[i] * ( sum{j in 1..m} ( w[j] * x[i,j] )+gamma) +s[i]>= 1;
	
subject to positive{i in 1..n}:
	s[i]>=0;