'''
 Write a function to generate all prime numbers up to 50.
'''
def prime():
    n = int(input("Enter Number : "))
    res = []

    for num in range(50,n+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            res.append(num)           
    print(res)
    
prime()