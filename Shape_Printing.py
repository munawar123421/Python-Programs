n=4
print("left sided pyramid----------------->")
for i in range(0,5):
    for i in range(n,5):
        print("*",end=" ")
    n-=1
    print("\n")
n=0
print("lower left sided pyramid----------------->")
for i in range(0,5):
    for i in range(n,5):
        print("*",end=" ")
    n+=1
    print("\n")
n=1
j=4
print("right sided pyramid----------------->")
for i in range(0,5):
    for i in range(n,5):
        print(" ",end=" ")
    for i in range(j,5):
        print("*", end=" ")
    j-=1
    n+=1
    print("\n")
n=5
j=5
print("lower right sided pyramid----------------->")
for i in range(0,5):
    for i in range(j,5):
        print(" ",end=" ")
    j -= 1
    for i in range(0,n):
        print("*", end=" ")
    n-=1
    print("\n")
print("Normal pyramid----------------->")
print("    *    \n")
print("   * *   \n")
print("  * * *  \n")
print(" * * * * \n")
print("* * * * *\n")