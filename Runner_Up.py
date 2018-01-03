"""
INSTRUCTIONS: 
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up 
score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2<= n <= 10
&
-100<= A[i] <= 100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

Explanation 0

Given list is [2 3 6 6 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score. 
"""


print("ehl")
n = int(input("example n:"))
arr = map(int, input("arr : ").split())
runner_up = 0
for item in arr:
    if item > runner_up:
        runner_up = item
for item in arr:
    arr.remove(runner_up) #I don't know how to remove something from a map because this doesn't work
for item in arr:
    if item > runner_up:
        runner_up = item    
print(runner_up)
