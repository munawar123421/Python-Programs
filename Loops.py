print("<_____________________Loops in python___________________>")
print("<________while loops________>")
#while True:
#    print("hello world")
i=1
while i<=5:            #iteration
    print("hello world")
    i+=1               #iterator
print(i)
i=1
while i<6:
    print(i)
    i+=1

#practice questions
#WAP NO.1
print("printing the numbers from 1 to 100")
i=1
while(i<101):
    print(i)
    i+=1

#WAP NO.2
print("printing the numbers from 100 to 1")
i=100
while(i>0):
    print(i)
    i-=1

#WAP NO.3
print("printing the multiplication table of number n")
num1=int(input("enter any number :"))
i=1
while(i<=10):
    print(num1*i)
    i+=1

#WAP NO.4
print("printing the element present in the list using while loop")
list1=[1,4,9,16,25,36,49,64,81,100]
i=0
while (i<10):
    print(list1[i])
    i+=1
#WAP NO.5
print("search for specific element from the tuple")
tuple1=(1,4,9,16,25,36,49,64,81,100)
x=100
i=0
while(i<10):
    if(tuple1[i]==x):
        print("present at index",i)
        break
    else:
        print("finding....")
    i += 1
i=1
while(i<=5):
    print(i)
    if(i==3):
        break      #break statement in python terminate when condition is True
    i+=1
i=0
while(i<5):
    if(i==3):
        i+=1
        continue    #continue statement shift i to next iteration and skip previous iteration
    print(i)
    i+=1
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1


