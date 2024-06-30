print("<_________________________Recursions in python________________________>")
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end")
show(5)

def factorial(n):
    fact=1
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
n=int(input("enter any number :"))
print("factorial of the given number is :",factorial(n))

#WAF NO.1 for finding the sum of n natural numbers
def sumfun(n):
    if n==0:
        return 0
    return n+sumfun(n-1)
sum=sumfun(4)
print(sum)

#WAF NO.2 for printing the list of element
def print_list(list,idx):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list([2,3,4,5],0)



