n=input("Enter value of n: ")
fact=1
if n<0:
    print "cant print value"
elif n==0:
    print "factorial of ",n," is 1"
else:
    for i in range(1,n+1):
        fact=fact*i
    print "The factorial of",n,"is ",fact
