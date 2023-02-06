from pprint import pprint

# First question : 
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



# Question 2

def dot_product(a,b):	
	if(len(a) != len(b) or len(a) ==0 or len(b) ==0 ):
		print("The input is not well-defined.")
	product = 0
	for i,  a_i in enumerate(a):
		b_i= b[i]
		product += a_i*b_i
	return product	


# Question 3
lines_in_normalized_form ={}
def find_normalized_coor(p1,p2):
	if len(p1) != 2 or len(p2)  != 2  or max(p1[0] , p1[1]) >104  :
		print("The points are not well-defined.")
	if p2[0] == p1[0]:
		slop = "inf"
		image_at_0 = "inf"
	else:	
		slop = (p2[1] -p1[1])/(p2[0] - p1[0])	
		image_at_0 = p1[1] - p1[0]*slop
	key = (slop , image_at_0)
	if key not in   lines_in_normalized_form:
		lines_in_normalized_form[key]  = [p1 , p2]
	else  :
		
		if p1 not in  lines_in_normalized_form[key] :lines_in_normalized_form[key].append(p1 )
		if p2 not in  lines_in_normalized_form[key] :lines_in_normalized_form[key].append(p2 )

def find_longest_point_chain(points):
	for i , pi in enumerate(points[:len(points)-1]):
		for j in range(i+1, len(points)):
			pj= points[j]
			find_normalized_coor(pi,pj)



	 	
class Segment:
	def __init__(self, A, lamb):
		self.A= A
		self.lamb = lamb
	def __init__(self, A, B):	









def f(n):
	return 5-n

points = [ (1,2), (2,4) , (3,6), (0,5), (5,0), (2,3) , (1,4), (4,1) ]
find_longest_point_chain(points)

pprint(lines_in_normalized_form)