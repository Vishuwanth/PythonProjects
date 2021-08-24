def getcomb(words,n):
    words = sorted(words)
    items = list(range(len(words)))
    old_comb = [[]]
    new_comb = []
    for i in range(n):
        new_comb = []
        for each in old_comb:
            for item in items:
                if (each and item > each[-1] ) or len(each) == 0:
                    new_comb.append(each + [item])
            old_comb = new_comb
    
    words_comb = []
    for each in new_comb:
        word_comb = []
        for index in each:
            word_comb.append(words[index])
        words_comb.append(tuple(word_comb))
    return sorted(set(words_comb))
words = input().split()


for i in range(1,len(words)+1):
    all_comb = getcomb(words,i)
    for each in all_comb:
        print(" ".join(each))