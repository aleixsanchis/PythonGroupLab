def collatz_prompt():
    print("Please select one of the parts to run: ")
    options = """    1. Print the Collatz sequence
    2. Find the longest Collatz sequence """
    print(options)
    opt=input("Enter choice: ")
    if (opt=="1"):
        collatz_print() 
    if (opt=="2"):
        collatz_sequence()

def collatz(n):
    if (n%2==0):
        return n/2
    else:
        return (n*3)+1

# Part 1: Printing the Collatz sequence
def collatz_print():
    n = int(input("Enter the starting number: "))
    while (n>1):
        print(int(n))
        n = collatz(n)
    print(int(n))

# Part 2: Finding long Collatz sequences
def collatz_sequence():
    n = int(input("Enter the maximum starting number: "))
    print("The longest sequence starting with numbers up to " + str(n) + " is ")
    max=0
    number=0     
    while (n>1):
        count=1
        temp=n
        while (n>1):
            count=count+1
            n = collatz(n)
        if (count>max):
             max=count
             number=temp
        n=temp-1
    
    print(str(number) + ", which is " + str(max) + " numbers long")
