n=int(input("enter a number: "))
i=0
a=0
b=1
s=0
print("   ")
for i in range(n):
    print(s, end=' ')
    a=b
    b=s
    s=a+b
