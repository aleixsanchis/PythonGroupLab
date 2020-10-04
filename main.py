import links
from collatz import *
from randomness import *
from factorial import *
options = """  1. Factorial
  2. Randomness
  3. Links
  4. Collatz"""  

def print_menu():
  print("This is the program from group 14!")
  print("Please select one of the features below, stop by entering Q.")
  print(options)

def main():
    opt=""
    while (opt!="Q"):
        print_menu()
        opt=input("Enter choice (stop with Q): ")
        if (opt == "1"):
          factorial_prompt()
        elif(opt == "2"):
          randomness_prompt()
        elif (opt == "3"):
          links.links_prompt()
        elif (opt=="4"):
          collatz_prompt()
    

if __name__ == "__main__":
    main()
