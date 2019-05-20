#This is an iterative function to identify whether a number is prime
def is_prime(num):
    divisor = 2
    while divisor < num:
        if num // divisor == 0:
            return False
        divisor = divisor + 1
    return True
    
#Tests    
print(is_prime(7))
print(is_prime(2))
print(is_prime(83))
print(is_prime(16))
