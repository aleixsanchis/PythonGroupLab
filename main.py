import links
import collatz
from collatz import collatz_print

def main():
    print("This is the program from group 14!")
    print("Please select one of the features below, stop by entering Q.")
    options = """    1. Factorial
    2. Randomness
    3. Links
    4. Collatz"""
    print(options)

    opt=""
    while (opt!="Q"):
        opt=input("Enter choice (stop with Q): ")
        if (opt=="4"):
            collatz_print()
    

if __name__ == "__main__":
    main()