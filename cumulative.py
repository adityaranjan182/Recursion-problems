def cumu(lst,n=1):
    if n==len(lst):
        return
    else:
        lst[n]=lst[n]+lst[n-1]
        return cumu(lst,n+1)

l=[1,2,3,4,7]
cumu(l)
print(l)