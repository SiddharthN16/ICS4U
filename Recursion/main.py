from sumDigits import iterativeCalculate as sumIterative
from sumDigits import recursiveCalculate as sumRecursive

from palindromes import iterativeCalculate as palindromeIterative
from palindromes import recursiveCalculate as palindromeRecursive

from mirrordromes import iterativeCalculate as mirrordromeIterative
from mirrordromes import recursiveCalculate as mirrordromeRecursive

# Driver Code - Problem 1: Sum Digits
n = 126
print(f"Problem 1 - Iterative: {sumIterative(n)}")
print(f"Problem 1 - Recursive: {sumRecursive(n)}")

# Driver Code - Problem 2: Palindromes
s = "kAyAK"
print(f"\nProblem 2 - Iterative: {palindromeIterative(s)}")
print(f"Problem 2 - Recursive: {palindromeRecursive(s)}")

# Driver Code - Problem 3: Mirrordromes
s = "totally"
print(f"\nProblem 3 - Iterative: {mirrordromeIterative(s)}")
print(f"Problem 3 - Recursive: {mirrordromeRecursive(s)}")
