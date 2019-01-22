## Code to print a inverted traingle and a pyramid
'''
def upside_down_triangle(i,t=0):
	if i == 0:
		return 0
	else:
		print (' '*t + '*' * ((i*2)-1))
		return upside_down_triangle(i-1,t+1)
'''
t=0
for i in (5,4,3,2,1,0):
	print (' '*t + '*' * ((i*2)-1))
	t=t+1
	
# upside_down_triangle(5)
'''
i		t		
5		0	' '*(0) + '*' * ((5*2)-1))=
4		1	' '*(1) + '*' * ((4*2)-1))=
3		2	' '*(2) + '*' * ((3*2)-1))=
2		3	' '*(3) + '*' * ((2*2)-1))=
1		4	' '*(4) + '*' * ((1*2)-1))=
0		5	' '*(5) + '*' * ((0*2)-1))=

*********
 *******
  *****
   ***
    *
'''