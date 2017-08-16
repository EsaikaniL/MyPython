def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


def main():
    n=input("Enter the value ")
    print "factorial value is: ",recur_factorial(n)

if __name__=="__main__":
    main()

