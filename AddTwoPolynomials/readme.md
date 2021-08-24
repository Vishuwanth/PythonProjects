Add two polynomials
Given two polynomials A and B, write a program that adds the given two polynomials A and B.
Input

The first line contains a single integer M.
Next M lines contain two integers Pi, Ci separated with space, where Pi denotes power and Ci denotes co-efficient of Pi for polynomial A.
After that next line contains a single integer N.
Next N lines contain two integers Pj, Cj separated with space, where Pj denotes power and Cj denotes co-efficient of Pj for polynomial B.
Output

Print the addition of polynomials A and B.
The format for printing polynomials is: Cix^Pi + Ci-1x^Pi-1 + .... + C1x + C0, where Pi's are powers in decreasing order, Ci is co-efficient and C0 is constant, there will be space before and after the plus or minus sign.
If co-efficient is zero then don't print the term.
If the term with highest degree is negative, the term should be represented as -Cix^Pi.
For the term where power is 1 represent it as C1x instead of C1x^1.
If the degree of polynomial is zero and the constant term is also zero, then just print 0 to represent the polynomial.
For term Cix^Pi, if the coefficient of the term Ci is 1, simply print x^Pi instead of 1x^Pi.
Explanation

If M = 4 and for polynomial A
For power 0, co-efficient is 5
For power 1, co-efficient is 0
For power 2, co-efficient is 10
For power 3, co-efficient is 6.

If N = 3 and for polynomial B
For power 0, co-efficient is 1
For power 1, co-efficient is 2
For power 2, co-efficient is 4.
Then polynomial A represents "6x^3 + 10x^2 + 5", the polynomial B represents "4x^2 + 2x + 1" and the addition of A and B is "6x^3 + 14x^2 + 2x + 6"
