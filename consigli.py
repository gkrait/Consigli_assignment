from pprint import pprint
import math

# First question : 
""" returns the pair (min_point , min_value)
such that f(min_point)= min_value
and min_value = min {f(x) : x in list}

list: a non-empty list of numbers
f: a function R -> R
 """
def find_min(list , f):
	if len(list) == 0 or len(list)>100:
		print("The list cannot be empty or of length > 100.")
	min_point=list[0]
	min_value = f(list[0]) 
	for element  in (list[1:]):
		if f(element) < min_value: 
			min_point = element
			min_value = f(element)	

	return ( min_point , min_value )		

"""
Asymptotic analysis: 
Since the input list is of limited length  <=100, the runnung time depends only on the cost of evaluating the function f at a point a.
Hence, if O(F) denotes the running time of evaluating the function f at a point a, then the running time  of the above algorithm is of order 100 O(F) = O(F).
On the other hand, if the length n of the list is not limted, then the running time is of order O(nF)   
"""

# Question 2

def dot_product(a,b):	
	if(len(a) != len(b) or len(a) ==0 ):
		raise Exception("The input is not well-defined.")
	product = 0
	for i,  a_i in enumerate(a):
		b_i= b[i]
		product += a_i*b_i
	return product	


# Question 3
"""  
The idea is to write every line in R2  in its slope-intercept form (y=mx +b), that is, to characterize it 
by a pair of scalars (m,b). As an exception, the lines parallel to Y-axis are stored as (infinity, b)
Hence, the main steps of the algorithm are:

1.   Define a dictionary where the goal of this dictionary is to map every line (represented by (m,b)) to a list of points that lay on that line.
2.   For each distinct pair of points p1, p2, compute the corresponding line pair  (m,b) and store p1, p2 in the corresponding list using the dictionary.
3.   Find the line with the longest list of points
"""




def assign_points2lines(p1,p2, lines_in_normalized_form):
	""" this function takes a pair of points p1, p2 and returns the pair (m,b) where y=mx +b is the line that transverse p1 and p2."""

	#  trivial input check: 
	if(p1 == p2):
		raise Exception( "No line can be defined using one pint") # if p1 == p2, do nothing. No line is defined 
	if len(p1) != 2 or len(p2)  != 2  or max(p1[0] , p1[1], p2[0], p2[1]) >104   or min(p1[0] , p1[1], p2[0], p2[1]) < -104  :
		raise Exception( "The input cintradicts the assumptions.")

	# if the line p1p2 is parallel to Y-axis, the line is ("infinity" , p1[0]) since the equation is x= p1[0]  
	if p2[0] == p1[0]:
		m = "infinity"
		b = p1[0]
	# if the slop exists, store the line as two numbers (m,b)
	else:	
		m = (p2[1] -p1[1])/(p2[0] - p1[0])	
		b = p1[1] - p1[0]*m
	key = (m , b)
	if key not in   lines_in_normalized_form:
		lines_in_normalized_form[key]  = [p1 , p2]
	else  :
		
		if p1 not in  lines_in_normalized_form[key] :lines_in_normalized_form[key].append(p1 )
		if p2 not in  lines_in_normalized_form[key] :lines_in_normalized_form[key].append(p2 )
	return (m,b)	



def find_longest_point_chain(points):
	if len(points) < 2 or len(points) > 300:
		print("points must cardinality between 2 and 300")
	# mapping lines to the corresponding list of points
	lines_in_normalized_form ={}
	for i , pi in enumerate(points[:len(points)-1]):
		for j in range(i+1, len(points)):
			pj= points[j]
			assign_points2lines(pi,pj ,lines_in_normalized_form)
	# finding the longest list among the values of lines_in_normalized_form
	longest_list = []
	line_with_max_points = ("Na","Na")
	for line, points in lines_in_normalized_form.items():
		if len(points) > len(longest_list):
			longest_list = points
			line_with_max_points = line


	print("the line y=" + str(line[0]) + " x + (" + str(line[1])  + ") has the longes list with "  + str(len(longest_list)) + " points"	 )	
	return 	len(longest_list)


# Question 4
class point:
	error_tolerance =0.000001 # because of the rounding error, any value v that is 0 < =v < error_tolerance  is assumed to be zero 
	def __init__(self, x,y ): 
		self.x=x 
		self.y = y
	def __eq__(self, other):
		
		return  abs(self.x - other.x) <  point.error_tolerance  and abs(self.y - other.y) < point.error_tolerance
	def __add__(self, other):
		return point(self.x+ other.x , self.y + other.y)
	def __rmul__(self, other):
		return point(self.x * other , self.y *other )

	def __str__(self):
		return "("+ str(self.x) + "," + str(self.y) + str(")")
	def norm(self):
		return math.sqrt( self.x**2 + self.y**2  )

class segment:
	def __init__(self, A,B ):
		if(A == B ):
			raise Exception("The segment cannot have equale endpoints")
		self.A= A 
		self.lamb= 	B  + (-1* A)
		self.B = B # The attribute B is redundant but it is useful for the comparison  operators

	def __eq__(self, other):
		return (self.A == other.A and self.B == other.B) or\
		 (self.A == other.B and self.B == other.A)
	def is_parallel_with(self, other):
		return   (other.lamb.norm()) * self.lamb ==   (self.lamb.norm()) * other.lamb   
	def in_the_same_line(self, other):
		return assign_points2lines( [self.A.x , self.A.y] , [ self.B.x, self.B.y] ,{} ) \
		== assign_points2lines( [other.A.x , other.A.y] , [ other.B.x, other.B.y], {} )
	def contains(self, other):
		bounsX = [ min(self.A.x , self.B.x ) , max(self.A.x , self.B.x )  ]
		bounsY = [ min(self.A.y , self.B.y ) , max(self.A.y , self.B.y )  ]
		return self.in_the_same_line(other) and\
		 bounsX[0] <= other.A.x <= bounsX[1] and \
		 bounsX[0] <= other.B.x <= bounsX[1] and \
		 bounsY[0] <= other.A.y <= bounsY[1] and \
		 bounsY[0] <= other.B.y <= bounsY[1]
	def get_k_distance(self , k):
		if(  k < 0 or  k > 1 ):
			raise Exception("k mist be in the interval [0,1]/")
		# is the k-distance is always taken with respect to the first point? 
		return self.A + k* self.lamb   

		

		
		




