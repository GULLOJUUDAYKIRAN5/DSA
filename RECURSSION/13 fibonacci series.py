# def fibo(n):
#     if n<=1:
#         return n
#     return fibo(n-1)+fibo(n-2)
# print(fibo(5))

def fibo(n,k):
    if n in k:
        return k[n]
    if n<=1:
        return n
    k[n]= fibo(n-1,k)+fibo(n-2,k)
    return k[n]
print(fibo(5,{}))