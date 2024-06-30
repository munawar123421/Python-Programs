# print("If Else statements in python".center(55,"-"))
#conditional operators
# >, <,>=,<=,==,!=
# agefind=int(input("enter any number:"))
# print(agefind)
# print("conditional operators in python............")
# print(agefind==18)
# print(agefind>=18)
# print(agefind<=18)
# print(agefind!=18)
# print("conditional statements in pyth0n:...........")
#example no.1
# age=input("enter your age:")
# age=int(age)                #explicit typecasting
# if age>18:
#   print("age of person is:",age)
#   print("you are old enough to drive")
# else:
#   print("you are not old enough to drive")
#example no.2
# num=input("enter 
# if num>=20:  any number:")
# num=float(num) #here interprator automatically do implicit typecasting(20 to 20.0).
#   print("entered number is=",num)
#   print("number is equal or greater than 20.0")
# elif num<20 and num>10:
#   print("entered number is=",num)
#   print("number is between 10.0 and 20.0")
# elif num<=10 and num>=0:
#   print("entered number is=",num)
#   print("number is included between 0.0 and 10.0")
# else:
#   print("entered number is=",num)
#   print("number is less than 0.0")
# print("i am happy now")
#nested if else  statements in python
print("nested if else statements in python".center(55,"-"))
num=float(input("enter any number:"))
if (num>=1000):#round brackets are optional
  if (num==1000):
    print("you are genius student")
  elif (num<=1100):
    print("you can deserve this scholarship")
  elif (num>1100 and num<=1200):
    print("you can deserve more as compared to other for this scholarship")
  else:
    print("you are out of our class/range for this scholarship")
elif (num<1000 and num>=800):
  if (num>=900):
    print("also an intelligent student")
  else:
    print("hardworking student")
else:
  print("student of low level & do more hardwork to gain good job")
