
# Asterisk Pattern
n = int(input("Enter a number : "))
print("\n\n~~~Asterisk Pattern~~~")

for i in range (1, n+1):
    for j in range (i):
        print("*", end = ' ')
    print("")

#Number Pattern 1
print("\n\n~~~Number Pattern 1~~~")

for i in range (1, n+1):
    for j in range (1, i+1):
        print(j, end = ' ')
    print("")

#Number Pattern 2
print("\n\n~~~Number Pattern 2~~~")

for i in range (1, n+1):
    for j in range (1, i+1):
        print(i, end = ' ')
    print("")

#Diamond Pattern
print("\n\n~~~Diamond Shape~~~")

for i in range (10):
    for j in range(10, i, -1 ): 
        print(" ", end = '')

    for k in range(i):
        print("* ", end = '')

    print("")


for i in range (10):
    for j in range(i):
        print(" ", end = '')

    for k in range(10, i, -1 ): 
        print("* ", end = '')    

    print("")
