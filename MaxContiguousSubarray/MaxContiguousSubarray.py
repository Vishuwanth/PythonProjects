num_list = list(map(int ,input().split()))

if not num_list:
    print(0)
else:
    sum_dict = {}
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)+1):
            sum_dict[tuple(num_list[i:j])] = sum(num_list[i:j])
    keys = list(sum_dict.keys())
    values = list(sum_dict.values())
    max_sum__index = values.index(max(values))
    print(*keys[max_sum__index])