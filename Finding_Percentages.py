"""
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, 
Physics and Chemistry. The marks can be floating values. The user enters some N integer followed by the names 
and marks for N students. You are required to save the record in a dictionary data type. The user then enters 
a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer N, the number of students. The next N lines contains the name and marks 
obtained by that student separated by a space. The final line contains the name of a particular student previously 
listed.

Constraints (These Constraints are also for the robot's input. Not our code)
2<=N<=10
0<=Marks<=100

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output

56.00

Explanation

Marks for Malika are 52 56 60 whose average is (52 56 60)/3 --> 56
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #asterisk shows that the rest of the split items will be saved in line
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    total = 0
    p=0
    for score in scores:
        total += score
        p +=1
    average = total/p
    print("%.2f"%average)
