def plusMinus(arr):
    pos_count=0
    neg_count=0
    zero_count=0
    for i in arr:
        if i>0:
            pos_count+=1
        elif i<0:
            neg_count+=1
        else:
            zero_count+=1
    pos_count=pos_count/n
    neg_count=neg_count/n
    zero_count=zero_count/n
    print(pos_count)
    print(neg_count)
    print(zero_count)
    
        

n = 5
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
        