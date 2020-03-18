
ch=4; s=8
def st(b,a):
    c=b
    if a==0: return (1)    
    for x in range (1,a):
        c*=b
        
    return c
print (st(ch,s),ch**s)

def rec(ch,s):
    
    if s>0:
        if s%2==1 : return (rec (ch,s-1)*ch)
        else: return (rec (ch*ch,(s-1)/2)*ch)



    else: return (1)

    
    

print (rec(ch,s))
    


