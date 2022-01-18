def iterativeCalculate(s):
	s = s.lower()
	total = 0
	singles = ['i', 'l', 'm', 'n', 'o', 't', 'u', 'v', 'w', 'x']
	mirrors = {"b": "d","p": "q","s": "z","d": "b","q": "p","z": "s"}

	def iterativeHelper(begin, end):
		count = 0
		while (begin >= 0 and end < len(s)):
			if ((s[begin] == s[end] and s[begin] in singles and s[end] in singles) or (s[begin] in mirrors and s[end] == mirrors[s[begin]])):
				count += 1
				begin -= 1
				end += 1
			else:
				break

		return count

	for i in range(len(s)):
		# Checking for Odd Length Mirrordromes
		total += iterativeHelper(i, i)

		# Checking for Even Length Mirrordromes
		total += iterativeHelper(i, i+1)
		
	return total

def recursiveCalculate(s):
    s = s.lower()
    i = -1
    total = 0

    singles = ['i', 'l', 'm', 'n', 'o', 't', 'u', 'v', 'w', 'x']
    mirrors = {"b":"d", "p":"q", "s":"z", "d":"b", "q":"p", "z":"s"}

    def mirrordromeCount(begin,end):
        if ((begin < 0 or end >= len(s)) or (s[begin] != s[end] or s[begin] not in singles or s[end] not in singles) and (s[begin] not in mirrors or s[end] != mirrors[s[begin]])):
            return 0

        return 1 + mirrordromeCount(begin-1, end+1)

    def recursiveCounter(i,total):
        if (i >= len(s)-1):
            return total
        else:
            i += 1

			# Checking for even & odd length mirrordromes
            total += mirrordromeCount(i,i) + mirrordromeCount(i,i+1)

            return recursiveCounter(i,total)

    return recursiveCounter(i,total)
