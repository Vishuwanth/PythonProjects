Given a list of integers, write a program to identify contiguous sub-list that has the largest sum and print the sub-list. Any non-empty slice of the list with step size 1 can be considered as contiguous sub-list.
Input

The input will contain space-separated integers, denoting the elements of the list.
Output

The output should be space-separated integers.
Explanation

For example, if the given list is [2, -4, 5, -1, 2, -3], then all the possible contiguous sub-lists will be,
[2]
[2, -4]
[2, -4, 5]
[2, -4, 5, -1]
[2, -4, 5, -1, 2]
[2, -4, 5, -1, 2, -3]
[-4]
[-4, 5]
[-4, 5, -1]
[-4, 5, -1, 2]
[-4, 5, -1, 2, -3]
[5]
[5, -1]
[5, -1, 2]
[5, -1, 2, -3]
[-1]
[-1, 2]
[-1, 2, -3]
[2]
[2, -3]
[-3]

Among the above contiguous sub-lists, the contiguous sub-list [5, -1, 2] has the largest sum which is 6. So the output should be 5 -1 2
