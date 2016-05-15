import math;
def make_circle(radius, precision=None):
	# returns a list of points (x,y) starting with (radius, 0)
	# arrayed about the origin in clockwise order.
	# precision = number of points. NB: (precision % 4) == 0
	if precision is None or precision<128:
		per_quad = 32;
	else:
		per_quad = precision/4;

	circ = [];
	for i in range(0, per_quad):
		# First quad
		theta = (math.pi * i)/(2 * per_quad);
		circ.append((radius * math.cos(theta), 
					 radius * math.sin(theta)));
	for i in range(1, 4):
		# Now rotate every point in the first quad thru (i*pi)/2
		last_zero = (i-1) * (per_quad);
		for j in range(0, per_quad):
			# x = -y'; y = x';
			x = circ[last_zero+j][1] * -1;
			y = circ[last_zero+j][0];
			circ.append((x, y));
	return circ;