# 此方法太慢會TLE
# class Solution:
#     def isPrime(self, num):
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True

#     def countPrimes(self, n: int) -> int:
#         count = 0
#         if n == 0 or n == 1:
#             return 0
#         for i in range(2, n):
#             if self.isPrime(i):
#                 count += 1
#         return count

'''
Sieve of Eratosthenes
Time Complexity: O(n log log n)
Space Complexity: O(n)
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
                
        p = 2
        while p*p < n:
            if is_prime[p]:
                for i in range(p*p, n, p):
                    is_prime[i] = False
            p += 1

        return sum(is_prime)
