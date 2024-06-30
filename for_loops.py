print("<_____________________Loops in python___________________>")
print("<________for loops________>")
#for loops works to move in a sequence
list1=[1,2,3,4,5]
for i in list1:    #in keyword used to find element from the specific list or string
    print(i)
name="munawar"
for i in name:
    if(i=="t"):
        print("character w found")
        break
    print(i)
else:
    print("end")

#practice questions
#WAP NO.1
list1=[1,4,9,16,25,36,49,64,81,100]
for i in list1:
    print(i)

#WAP NO.2
list1=[1,4,9,16,25,36,49,64,81,100]
search=list1[4]
for i in list1:
    if(i==search):
        print("found the value :",i)
        break
    else:
        print("finding...")

print("...........range function in python.............")
for i in range(5):      #5 is the ending index and starting index bydefault is 0
    print(i)
for i in range(3,6):    #we give manually start and stop condition
    print(i)
for i in range(1,20,4): #we give start, stop and steps value in iteration
    print(i)

#practice questions
#WAP NO.1
for i in range(1,101):
    print(i)

#WAP NO.2
for i in range(100,0,-1):
    print(i)
#WAP NO.3
num=int(input("enter any number :"))
print(num)
for i in range(1,11):
    print(num*i)

for i in range(3):
    pass                #it acts as a placeholder for future use
print("hello world")

#practice tasks
#WAP NO.1 for sum of numbers enter by the user using while loop
num1=int(input("how many numbers you want to perform sum :"))
print(num1)
sum=0
i=0
while(i<num1):
    num2=int(input("enter your number :"))
    sum=sum+num2
    i+=1
print("sum of numbers is :",sum)

#WAP NO.2 for factorial for number enter by the user using for loop
n=int(input("enter number to check factorial for it :"))
print(n)
fact=1
for i in range(n,0,-1):
    fact=i*fact
print("factorial of number is :",fact)



