#strings are immutable(not changed)
print("Methods of strings".center(60,"."))
name = "Munawar"
name1 = "Munawar Ali Khan"
#length of string in python
print("1.length of strings=")
print(len(name))
print(len(name1))
#convert string to uppercase and lowercase
print("\n2.printing the string name to upper as well as lower case letter=\n")
print(name)
print(name.upper())
print(name.lower())
print(name1)
print(name1.upper())
print(name1.lower())
#replace the string with original string
print("\n3.replacing the string name with original string=\n")
print(name1.replace("Khan", "khani"))
print(name1)  #not changing value of original variable
print(name.replace(name, "python programmer"))  #just for one command only
print(name)
#find the string used to find the index of string
print("\n4.finding the index of string=\n")
print(name.find("namal university"))  #if value not present then return -1
print(name.find('a'))
print(name.find('r'))
print(name1.find('Ali'))
print(name1.find('Muhammad Munawar Khan'))
print(name1.find('n'))  #if value is repeated give first index of value
print(name1.find('n', 11))
#print(str6.index("namal university"))#show error if value is not present
print("\n5.printing the string in split way=\n")
print(name1.split(" "))
print("\n6.printing the string in capital way=\n")
str3 = "how are you brother"
print(str3.capitalize())
print("\n7.printing the string first letter capital=\n")
print(str3.title())
print(
    "\n8.printing the string is in title form (first letter of every word is greater and all other letters are small=\n"
)
str5 = ("What Is Your Father Name")
print(str5.istitle())
print(str3.istitle())
print("\n9.printing the string at center=\n")
print(str3.center(60))
print(str3.center(55, '-'))
str4 = "welcome to this console"
print(str4.center(55, "."))
print("\n10.printing the count of string=\n")
print(str4.count('to'))
print(str4.count('console'))
str6 = "munawar khan munawar g munawar"
print(str6.count('munawar'))
print("\n11.printing the count of string lies of following range=\n")
print(str6.count('munawar', 0, 25))
print(str6.count('munawar', 0, 30))
print(str6.count('munawar', 0, 15))
print("\n12.printing the end of string in true or false=\n")
print(str6.endswith('g', 2, 30))  #finding the string in range
print(str6.endswith('khan', 2, 12))
print("\n13.printing the string in true or false=\n")
print("1...for alphanumeric:")
str7 = "heisa123"
print(str7.isalnum())  #used for checking the string in alphanumeric
print(name.isalnum())
print("2...for alpha:")
print(name.isalpha())  #uded for checking the string in alphabet
print(str7.isalpha())
print("\n14.printing the string in true or false=\n")
print("1...for lower:")
print(name.islower())#check whether the string is lower or not.
print(str6.islower())
print("2...for upper:")
print(str6.isupper())
str8="PYTHONPROGRAMMING"
print(str8.isupper())
print("\n15.check whether the string is printable or not true or false=\n")
print(str8.isprintable())
print(str7.isprintable())
print(str6.isprintable())
print(str5.isprintable())
print(str4.isprintable())
str9="ttt\n"     #This \n is not printable
print(str9.isprintable())
str10="munawar from \"mochh\""
print(str10)
print(str10.isprintable())
print("\n16.check whether the string has white spaces result true or false=\n")
print(str10.isspace())
str11="    "#if spaces are 1 or more than 1 then result is true else 0.
print(str11.isspace())
print(name.isspace())
print("\n17.check whether the string starts with result true or false=\n")
print(str8.startswith("PYTHON"))#takes starting letter and check with given letter
print(str8.startswith("python"))
print("\n18.swap case of string=\n")
print(str8.swapcase()) #swapcase convert uppercase to lowercase and lowercase to uppercase
print(str6.swapcase())
print(name1.swapcase())

