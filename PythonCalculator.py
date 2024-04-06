def sum(x,y):
    res = x+y
    print(f'The sum of {x} and {y} is {res} ')

def sub(x,y):
    res = x-y
    print(f'The subtraction of {x} and {y} is {res}')

def mul(x,y):
    res = x*y
    print(f'The multiplication of {x} and {y} is {res}')

def div(x,y):
    res = x/y
    print(f'The division of {x} and {y} is {res}')
    
     
x = int(input('Enter number 1: '))
y = int(input("Enter number 2: "))
choice = int(input('''Enter your choice as belows: 
                   SUM : 1
                   SUB : 2
                   PRODUCT : 3
                   DIVISION : 4
                   '''))
if(choice==1):
    sum(x,y)
if(choice==2):
    sub(x,y)
if(choice==3):
    mul(x,y)
if(choice==4):
    div(x,y)
else:
    print("Wrong input")