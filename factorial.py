def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number: "))
x=1
while x<=n:
  outp1="{}! = {}"
  print(outp1.format(x,factorial(x)))
  x=x+1
# Digits in factorials

def frequencyDigits(n, d):
  c = 0;
  while (n > 0):
    if (n % 10 == d):
      c += 1;
      n = int(n / 10);
      return c; 
  
N = int(input("Enter the maximum n to compute n! for: "))
D = int(input("Enter a single digit: "))
def factorial(m):
  if m == 0:
    return 1
  else:
    return m * factorial(m-1)
outp2="{}! = {}"
print(outp2.format(N,factorial(N)))

# Factoring factorials

number=int(input("Enter a number: "))
print(str(number) + "! = " + "*".join(str(n) for n in range(1, number + 1)))
