class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        def checkPrime(num):
            
            isPrime = True
            for i in range(2, num):
                if num%i == 0:
                    isPrime = False
                    break
            
            return isPrime
        
        def factorial(num):
            ans = 1
            for i in range(1, num+1):
                ans = ans*i
            
            return ans
        
        no_of_Not_Prime = 1
        no_of_Primes = 0
        
        for num in range(2, n+1):
            if checkPrime(num):
                no_of_Primes += 1
            else:
                no_of_Not_Prime += 1
        
        num1 = factorial(no_of_Not_Prime)
        num2 = factorial(no_of_Primes)
        
        return (num1 * num2) % ((10**9) + 7)