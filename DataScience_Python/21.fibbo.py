#WAP to print n number of terms in a fibbonaci series using function

def fibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return(fibo(n-1)+ fibo(n-2))

n = int(input("Enter number of terms: "))
i = 0
while(i<n):
    print(fibo(i), end=" ")
    i+=1