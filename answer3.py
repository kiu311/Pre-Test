def nextFib(x):
    a,b = 1,1
    while b <= x:
        temp = b;
        b = a + b;
        a = temp; 
    return b
  
def nextFibonacci(array):
    return [ nextFib(x) for x in array]
