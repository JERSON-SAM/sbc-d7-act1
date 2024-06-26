'''num1 = int(input("num1:"))
num2 = int(input("num2:"))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
'''
'''
def jerson():
    return 1+1

def sub():
    print(1-1)

num = jerson()
num2 = sub()

print(num)
print(num2)
'''
'''
def add(x):
    print(x  + 1)

i = 142
add(i)
'''
'''
def triangle(b1,b2,g1):
    print(f"{b1} likes {g1}")
    print(f"{b2} likes {g1}")

triangle (b2="bertox", b1="don lowell", g1="marjore")    

def names(*args):
    for arg in args:
        print(arg)
names ("bertox", "don", "jonathan", "Marjore")   
'''     

def names(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} ~ {value}")

names(Paloma="Airon", Bubbles="Daniel")