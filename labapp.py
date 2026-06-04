print("this is example app")
print("a=15,b=10")
a=15
b=10
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
a,b=swap(a,b)
print(f"a={a},b={b}")