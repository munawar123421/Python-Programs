#strings in python are surrounded by either single quotation marks, or double quotation marks
str1="munawar"
str2="khani"
print(str1,str2) #using default seperator
print(str1+str2) #concatenation
print(str1*3) #replication
print("muhammad "+str1)
print("muhammad "+str1+" "+str2)
str3="i am from mochh mianwali. i am a student of class 14th in namal university in computer science department."
print(str3)
str3="i am from mochh mianwali. i am a student of \n\"class 14th in namal university\" in computer science department."  #using escape sequence character
print(str3)
str3="i am from mochh mianwali. i am a student of \t\"class 14th in namal university in computer science \tdepartment."#used for one space
print(str3)
print("result to show values at index in str1=")
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
print("result of str2 using for loop=")
for character in str2:
  print(character)
print("result of str3 using for loop=")
for character in str3:
  print(character)
print("simple printing")
print("simple \tprinting")