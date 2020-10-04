def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_prompt():
  print("Please select one of the parts to run: ")
  options = """  1. Printing factorials
  2. Digits in factorials
  3. Factoring factorials"""
  print(options)
  opt=input("Enter choice: ")
  if (opt=="1"):
      factorial_print() 
  elif (opt=="2"):
      frequency_print()
  elif (opt=="3"):
      factorization_print()

def factorial_print():
  n=int(input("Enter a number: "))
  x=1
  while x<=n:
    outp1="{}! = {}"
    print(outp1.format(x,factorial(x)))
    x=x+1

def frequency_print():
  n = int(input("Enter the maximum n to compute n! for: "))
  d = int(input("Enter a single digit: "))

  frequency_digits(n,d)

def factorization_print():
  number=int(input("Enter a number: "))
  factorization(number)
# Digits in factorials
def frequency_digits(n, d):
  c = 0;
  while (n > 0):
    if (n % 10 == d):
      c += 1;
      n = int(n / 10);
      return c;
# Factoring factorials
def factorization(number):
  print(str(number) + "! = " + "*".join(str(n) for n in range(1, number + 1)))
