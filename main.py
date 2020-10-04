import links
from collatz import *
from randomness import *
def main():
    print("This is the program from group 14!")
    print("Please select one of the features below, stop by entering Q.")
    options = """    1. Factorial
    2. Randomness
    3. Links
    4. Collatz"""    

    opt=""
    while (opt!="Q"):
        print(options)
        opt=input("Enter choice (stop with Q): ")
        if (opt=="4"):
            collatz_prompt()
        elif(opt == "2"):
            randomness_prompt()
    

if __name__ == "__main__":
    main()