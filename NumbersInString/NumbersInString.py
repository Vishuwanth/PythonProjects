sentence = input()
#print(sentence)

def getNums(sentence):
    nums = []
    number = ""
    for each in range(len(sentence)):
        #print(sentence[each],sentence[each].isdigit())
        if sentence[each].isdigit():
            number += sentence[each]
        if each == len(sentence)-1:
            if number != '':
                nums.append(number)

        if each != 0:
            if sentence[each].isdigit() == False:
                 if sentence[each-1].isdigit():
                     nums.append(number)
                     number = "" 
                     continue;
    return nums

num = getNums(sentence) 
num_list = []
for each in num:
    num_list.append(int(each))
print(sum(num_list))
average = sum(num_list)/len(num_list)
print(round(average,2))