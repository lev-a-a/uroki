def gener (N:int, M:int,prefix=None):
    prefix=prefix  or []
    if M==0: print (prefix); return
    for dig in range (N):
        prefix.append(dig)
        gener (N,M-1,prefix)
        prefix.pop()


gener (2,2)
