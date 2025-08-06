def natural(i,sum,n):
    if i>n:
        print(sum)
        return
    natural(i+1,sum+i,n)

def nat(i,n):
    if i==n:
        return i
    x=i+nat(i+1,n)
    return x

natural(0,0,5)
print(nat(0,5))
    
