"""
Let's learn about list comprehensions!
You are given three integers X,Y and Z representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid
where the sum of i + j + k is not equal to N.
Here, 0 <= i <= X; 0 <= j <= Y, 0 <= k <= Z

Input Format:
Four integers X,Y,Z and N each on four separate lines, respectively.

Constraints:
Print the list in lexicographic increasing order.

Sample input:
1 (1 is max value, so 1st item will be 0 <= x <= 1 in every sublist)
2 (so 2nd item will be 0 <= y <= 2 in every sublist)
3 (so 3rd item will be 0 <= z <= 3 in every sublist)
4 (the total x + y + z != 4)

Sample output (this is an example but it is not in the correct order):
[([0,0,0], [0,0,1], [0,1,0], [1,0,0],) ([0,0,2], [0,1,1], [0,2,0], [1,0,1], [1,1,0],) [0,0,3],[0,1,2],
[0,2,1],[1,0,2], [1,1,1], [1,2,0], [0, 2, 3], [1,1,3],[1,2,2],[1,2,3]]

Concept
  You have already used lists in previous hacks. List comprehensions are an elegant way to 
  build a list without having to use different for loops to append values one by one. 
  This example might help.

Example: You are given two integers x and y . 
  You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to 
  n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the 
  code if we dont use list comprehensions in Python.
  
Solution:
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[ i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if k+j+i != n])
