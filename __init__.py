print("<_________________Sets in python_________________>")
set1={1,2,3,4}
print(set1)
set2={1,2,3,2,1}
print(set2)
set3={"mudasir",3,4.78,"khani","apple"}
print(set3)
set4=("dell",(1,2,3),1,"hp")
print(set4)
set5=("dell",(1,2,3),1,"hp",{"raees","aqeel",567})  #set within set
print(set5)
print(len(set5))        #it tells about the length of set
collection={}           #this is an empty dictionary not empth set
print(type(collection))
collection1=set()      #this is an empty set
print(type(collection1))
collection1.add(23)                #add function add the elements in the set
collection1.add("vivo y21")
collection1.add("sports")
collection1.add("sets")
print(collection1)
collection1.remove("vivo y21")     #remove function remove elements from the set
print(collection1)
#collection1.remove("munawar")      #it gives an key value error when element is not present in the set
#print(collection1)
collection1.discard("munawar")      #discard function doesnot gives an error when element is not present and when we print it then print it out.
print(collection1)
set1.clear()                        #clear function clear or empty the whole set
print(set1)
collection1.pop()                   #pop function removes the random value from the set
print(collection1)
collection1.pop()
print(collection1)
unionset1={1,3,4,5,7}
unionset2={3,4,2,9,0}
print(unionset1.union(unionset2))   #union set perform same union as we done in math
print(unionset1.intersection(unionset2))   #intersection same as well
value1={"munawar",34,22,90.89,"khani"}
value2={"khani","mudasir","physics",22,56}
print(value1.union(value2))
print(value1.intersection(value2))
#practice question

#WAP NO.1
dict1={
    "table":["a piece of furniture","list of facts& figures"],
    "cat":"a small animal"
}
print(dict1)

#WAP NO.2
set1={"python","java","c++","python","javascript"}
set2={"java","python","java","c++","c"}
print(set1.union(set2))
print(len(set1.union(set2)))

#WAP NO.3
dict1={}
phy_marks=input("enter the marks of physics :")
dict1.update({"physics":phy_marks})
print(dict1)
chm_marks=input("enter the marks of chemistry :")
dict1.update({"chemistry":chm_marks})
print(dict1)
bio_marks=input("enter the marks of biology :")
dict1.update({"biology":bio_marks})
print(dict1)

#WAP NO.4
forset={9,9.0}
print(forset)
forset1={9,"9.0"}
print(forset1)
forset3={               #this is the set not dictionary and set contain immutable value of tuple
    ("float",9.0),
    ("int",9)
}
print(forset3)


