import random

def randomness_prompt():
    print("Please select one of the parts to run: ")
    x=int(input("1.Throwing virtual dice \n2.Distribution of die results \n3.Graphical distribution of die results\n4.Loaded dice"))
    if (x==1):
        throwdice() 
    elif (x==2):
        distr()
    elif (x==3):
        graph()
    elif(x==4):
        loadedgraph()

#Part 1 : throwing the virtual dice
def throwdice():
    x =int(input("Enter a number of dice to throw: "))
    z=0
    for i in range(x):
        y=random.randint(1,6)
        z=z+y
        print("Die %d: %d"%(i+1,y))
    print("\nAverage: %f"%(z/x))

#Part 2 : Distribution of die results
def distr():
    x =int(input("Enter a number of dice to throw: "))
    y =int(input("Enter the number of trials: "))
    c =[0]*1000
    print("\n")
    for i in range(y):
        b=0
        for j in range(x):
            a=random.randint(1,6)
            b=b+a
        c[b]=c[b]+1
    for i in range(6*x+1):
        if(c[i] != 0):
            if(i<10):
                print(" %d: %d"%(i,c[i]))
            else:
                print("%d: %d"%(i,c[i]))

#Part 3 : Graphical distribution of die results
def graph():
    x =int(input("Enter a number of dice to throw: "))
    y =int(input("Enter the number of trials: "))
    c =[0]*1000
    for i in range(y):
        b=0
        for j in range(x):
            a=random.randint(1,6)
            b=b+a
        c[b]=c[b]+1
    for i in range(6*x+1):
        if(c[i] != 0):
            if(i<10):
                print("\n %d:"%(i),end=" ")
            else:
                print("\n%d:"%(i),end=" ")
            for j in range(c[i]):
                print("#",end="")


#Part 4 : Loaded dice

def loadedgraph():
    x =int(input("Enter a number of dice to throw: "))
    y =int(input("Enter the number of trials: "))
    c =[0]*1000
    for i in range(y):
        b=0
        for j in range(x):
            a=random.random()
            if(a<0.0833):
                b=b+1
            elif(a<0.2503):
                b=b+2
            elif(a<0.4173):
                b=b+3
            elif(a<0.5843):
                b=b+4
            elif(a<0.7513):
                b=b+5
            else:
                b=b+6
        c[b]=c[b]+1
    for i in range(6*x+1):
        if(c[i] != 0):
            if(i<10):
                print("\n %d:"%(i),end=" ")
            else:
                print("\n%d:"%(i),end=" ")
            for j in range(c[i]):
                print("#",end="")
