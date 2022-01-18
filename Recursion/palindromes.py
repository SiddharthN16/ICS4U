def iterativeCalculate(s):
    s = s.lower()
    total = 0

    def iterativeHelper(begin, end):
        count = 0
        while (begin >= 0 and end < len(s) and s[begin] == s[end]):
            count +=1
            begin -= 1
            end += 1

        return count

    for i in range(len(s)):
        # Checking for Odd Length Palindromes
        total += iterativeHelper(i-1,i+1)
		
        # Checking for Even Length Palindromes
        total += iterativeHelper(i,i+1)
		
    return total

def recursiveCalculate(s):
    s = s.lower()
    i = -1
    total = 0

    def palindromeCount(begin,end):
        if(begin < 0 or end >= len(s) or s[begin] != s[end]):
            return 0

        return 1 + palindromeCount(begin-1, end+1)

    def recursiveCounter(i,total):
        if (i >= len(s)-1):
            return total
        else:
            i += 1
			# Checking for even & odd length palindromes
            total += palindromeCount(i-1,i+1) + palindromeCount(i,i+1)
			
            return recursiveCounter(i,total)

    return recursiveCounter(i,total)
