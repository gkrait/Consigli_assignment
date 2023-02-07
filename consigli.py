from pprint import pprint

# First question : 
""" returns the pair (min_point , min_value)
such that f(min_point)= min_value
and min_value = min {f(x) : x in list}

list: a non-empty list of numbers
f a function R -> R
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

"""Asymptotic analysis: 
Since the input list is of limited length  <=100, the runnung time depends only on the cost of evaluating the function f at a point a.

Hence, if O(F) is the running time of evaluating the function f at a point a, then the running time  of the above algorithm is of order 100 O(F) = O(F).

On the other hand if the length n of the list is not limted, then the runningt time is of order O(nF)   

"""

# Question 2

def dot_product(a,b):	
	if(len(a) != len(b) or len(a) ==0 ):
		print("The input is not well-defined.")
	product = 0
	for i,  a_i in enumerate(a):
		b_i= b[i]
		product += a_i*b_i
	return product	


# Question 3
"""  
The idea is to write every line in R2  in its slope-intercept form (y=mx +b), that is, to charachtirize it 
by a pair of scalras (m,b). As an exception, the lines parallel to Y-axis are stored as (infinity, b)
Hence, the main steps of the algorithm are:
1) Define a dictinary. The goal of this dictinary is to map every line (represented by (m,b)) to a list of points that lay on that line.
2) For each distince pair of points p1, p2, compute the corresponding line pair  (m,b) and store p1, p2 in the coreesponding list using the dictinary. 
3) Find the line with the longest list of points
"""


lines_in_normalized_form ={}

def find_normalized_coor(p1,p2):
	""" this function takes a pair of points p1, p2 and returns the pair (m,b) where y=mx +b is the line that transverse p1 and p2."""

	#  trivial input check: 
	if(p1 == p2):
		return # if p1 == p2, do nothing. No line is defined 
	if len(p1) != 2 or len(p2)  != 2  or max(p1[0] , p1[1], p2[0], p2[1]) >104   or min(p1[0] , p1[1], p2[0], p2[1]) < -104  :
		print("The points are not well-defined.")
		return
	# if the line p1p2 is parallel to Y-axis, the lines is ("infinity" , p1[0]) since the equation is x= p1[0]  
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



def find_longest_point_chain(points):
	if len(points) < 1 or len(points) > 300:
		print("points must cardinality between 1 and 300")
	for i , pi in enumerate(points[:len(points)-1]):
		for j in range(i+1, len(points)):
			pj= points[j]
			find_normalized_coor(pi,pj)
	# finding the longest list among the values of lines_in_normalized_form
	longest_list = []
	line_with_max_points = ("Na","Na")
	for line, points in lines_in_normalized_form.items():
		if len(points) > len(longest_list):
			longest_list = points
			line_with_max_points = line


	print("the line y=" + str(line[0]) + " x + (" + str(line[1])  + ") has the longes list with "  + str(len(longest_list)) )		


# Question 4
class point:
	def __init__(self, x,y ):
		self.x=x 
		self.y = y
	def __eq__(self, other):
		return (self.x==other.x) and (self.y==other.y)
	def __add__(self, other):
		return point(self.x+ other.x , self.y + other.y)
	def __rmul__(self, other):
		return point(self.x * other , self.y *other )

	def __str__(self):
		return "("+ str(self.x) + "," + str(self.y) + str(")")

				




class Segment:
	def __init__(self, A,B ):
		self.A= A 
		self.B = B
		self.lamb= 	B  + (-1* A)

	def __eq__(self, other):
		return self.A == other.A and self.lamb == other.lamb



"""
points = [ (1,2), (2,4) , (3,6), (0,5), (5,0), (2,3) , (1,4), (4,1) ]
find_longest_point_chain(points)
#pprint(lines_in_normalized_form)"""

p1 = point(1,1)
p2 = point(2,2)

p3 = point(3,3)

L1 = Segment(p1,p2)
L2= Segment(p1,p3)

print(L1 ==L2  )
