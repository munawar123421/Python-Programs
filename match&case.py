#match case statements in python
print("match case statement in python".center(55,'-'))
x=int(input("please enter any number:"))
match (x):#works as a switch case statement
  case 0:
    print('The value of x is zero')
    #we used break statement  in c++ or c to break the loop after the first case is matched but in python no need of it.
  case 1:
    print('The value of x is one')
  case 2:
    print('The value of x is two')
  case 3:
    print('The value of x is three')
  case 4:
    print('The value of x is four')
  case _ if x==50:
    print('The value of x is 50')
  case _ if x==60:
    print('The value of x is 60')
  case _:#c++ or c used default keyword
    print('The value of x is is not present so value is :',x)
  
  




