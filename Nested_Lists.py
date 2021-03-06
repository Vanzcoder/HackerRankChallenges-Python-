"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the 
name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a 
new line.

Input Format

The first line contains an integer, N, the number of students.
The subsequent 2N lines describe each student over 2 lines; the first line contains a student's name, and the second 
line contains their grade.

Constraints
    2<=N<=5
    There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, 
order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry

Explanation

There are 5 students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their 
names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    list_outer = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_inner = [name, score]       
        list_outer.append(list_inner)
    
    #This finds min and max
    Min = 100
    Sec_lowest = 100
    Min_names = []
    Sec_names = []
    
    for item in list_outer:
      if item[1] < Min:
        Sec_lowest = Min
        Sec_names = Min_names
        Min = item[1]
        Min_names = [item[0]]
      elif item[1] == Min:
        Min_names.insert(0,item[0])
      elif item[1] < Sec_lowest:
        Sec_lowest = item[1]
        Sec_names = [item[0]]
      elif item[1] == Sec_lowest:
        Sec_names.append(item[0])

    for item in Sec_names:
      print(item)
