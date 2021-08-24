from collections import Counter

def polynomial(integer):
    polynomial_a = [] 
    for i in range(integer):
        Pi,Ci = input().split()
        Pi = int(Pi)
        Ci = int(Ci)
        polynomial_a.append((Pi,Ci))
    return polynomial_a

def addPolynomials(poly_a,poly_b):
    result = dict()
    if len(poly_a) > len(poly_b):
        maxi = poly_a
        mini = poly_b
    else:
        maxi = poly_b
        mini = poly_a
    #print(maxi)

    for each in maxi.keys():
        if each in mini.keys():
            result[each] = maxi.get(each) + mini.get(each)
        else:
            result[each] = maxi.get(each)
    
    output = list(result.items())
    output.reverse()
    output.sort(reverse=True)
    #print(output)
    
    final_poly = []
    sums = 0
    for each in output:
        sums += each[1]
    if sums==0:
        return 0
    else:
        for each in output:
            if (each[0] == maximum) and (each[0] != 0) and (each[0] != 1):
                if each[1] == 0:
                    continue
                elif each[1] == 1:
                    final_poly.append("x^"+str(each[0]))
                elif each[1] < 1:
                    final_poly.append("-"+str(abs(each[1]))+"x^"+str(abs(each[0])))
                else:
                    final_poly.append(str(each[1])+"x^"+str(each[0]))
            elif each[0] == 0 :
                if each[1] ==0:
                    continue
                elif each[1] <0:
                    final_poly.append(" - "+str(abs(each[1])))
                else:
                    final_poly.append(" + "+str(each[1]))
            elif each[0] == 1 :
                if each[1] == 0:
                    continue
                elif each[1] == 1:
                    final_poly.append("x")
                elif each[1] == -1:
                    final_poly.append(" - "+"x")
                elif each[1] < 0:
                    final_poly.append(" - "+str(abs(each[1]))+"x")
                else:
                    final_poly.append(" + "+str(each[1])+"x")
                
            elif each[0] != 0 and each[0] != maximum:
                if each[1] == 0:
                    continue
                elif each[1] == 1:
                    final_poly.append(" + "+"x^"+str(each[0]))
                elif each[1] == -1:
                    final_poly.append(" - "+"x^"+str(abs(each[0])))
                elif each[1] < 1:
                    final_poly.append(" - "+str(abs(each[1]))+"x^"+str(abs(each[0])))
                else:
                    final_poly.append(" + "+str(each[1])+"x^"+str(each[0]))
        return "".join(final_poly)

m = int(input())
poly_a=dict(polynomial(m));

n= int(input())
poly_b= dict(polynomial(n))

maximum= max(m,n)-1

print(addPolynomials(poly_a,poly_b))
