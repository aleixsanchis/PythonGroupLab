def collatz_print():
    n = int(input("Enter the starting number: "))
    while (n>1):
        print(int(n))
        if (n%2==0):
            n=n/2
        else:
            n=(n*3)+1
    print(int(n))
