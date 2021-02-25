'''n=int(input("Enter n value"))
for i in range(n):
    print("*", end=".")'''

'''n=int(input("Enter the value of n"))
for i in range(n):
    print("* " * n)'''
'''n=int(input("Enter the n value"))
for i in range(n):
    print((str(n)+" ")*n)'''
'''n=int(input("Ennter the n value"))
for i in range(n):
    print((str(i+1)+" ")*n)'''
'''n=int(input("Enter the n value"))
for i in range(n):
    print("A " * n)'''
'''n=int(input('Enter the n value'))
for i in range(n):
    print((chr(65+i)+' ')*(i+1))'''

'''n=int(input('Enter the n value'))
for i in range(n):
    print((chr(65+i)+' ')*n)'''

'''n=int(input("Enter the n value"))
for i in range(n):
    print((str(i+1)+" ")*(n-i) )'''

'''n=int(input("Enter the n value"))
for i in range(n):
    for j in range(n-i):
        print(j+1, end=" ")
    print()'''

'''n=int(input("Enetr the n value"))
for i in range(n):
    for j in range(n-(n-i)):
        print((str(j+1)+" ")*(i+1))
    print()'''

'''n=int(input("enterr row value"))
for i in range(n):
    print("* " * (i+1))
for i in range(n-1):
    print("* " *(n-i-1))'''

'''n=int(input("enter n value"))
for i in range(n):
    print('  '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print("  "*(i+1)+"* "*(n-i-1))'''

'''n=int(input("enterr the n value"))
for i in range(n):
    print('  '*(n-i-1)+'* ',end=" ")
    if i>=1:
        print('  '*(2*i-1)+"* ",end=" ")
    print()'''
'''n=int(input("enterr the n value"))
for i in range(n):
    print("  "*i+"* ",end=" ")
    if i!=n-1:
        print("  "*(2*n-2*i-3)+"* ",end=" ")
    print()'''

'''n=int(input("enterr the n value"))
for i in range(n):
    print("  "*i+ chr(65+i)+" ",end=" ")
    if i!=n-1:
        print("  "*(2*n-2*i-3)+ chr(65+i)+" ",end=" ")
    print()'''

'''n=int(input("enterr the n value"))
for i in range(n):
    print("  "*(n-i-1)+ chr(65+i)+" ",end=" ")
    if i>=1:
        print("  "*(2*i-1)+ chr(65+i)+" ",end=" ")
    print()'''

n=int(input("enterr the n value"))
for i in range(n):
    print("  "*(n-i-1)+ chr(65+i)+" ",end=" ")
    if i>=1:
        print("  "*(2*i-1)+ chr(65+i)+" ",end=" ")
    print()
for i in range(n):
    print("  " * i + chr(65 + i) + " ", end=" ")
    if i != n - 1:
        print("  " * (2 * n - 2 * i - 3) + chr(65 + i) + " ", end=" ")
    print()




