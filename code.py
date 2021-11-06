def find(a,x):
    if a == [] or (len(a) == 1 and a[0]!=x):
        return -1 
    index = round(len(a)/2)
    if(a[index] == x):
        return index
    elif(a[index] > x):
        return find(a[0:(index)],x) 
    else:
        r = find(a[(index+1):(len(a))],x)
        return -1 if r == -1 else index+r+1