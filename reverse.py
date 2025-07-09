def reverse(r):
    r=r[::-1]
    print(r)
    a=sum(r)
    print("sum:",a)
    print("Average",a/5)
    print(a)
l=[]
for i in range(5):
    n=int(input(f"Enter number {i+1}:"))
    l.append(n)
reverse(l)
