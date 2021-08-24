input_str = input().split()
first_int = int(input_str[0])
sec_int = int(input_str[-1])
operator = input_str[1]
#print(input_str)

if operator == "+":
    print(first_int +sec_int)
elif operator == "-":
    print(first_int - sec_int)
elif operator == "*":
    print(first_int * sec_int)
elif operator == "/":
    print(first_int / sec_int)
elif operator == "%":
    print(first_int % sec_int)