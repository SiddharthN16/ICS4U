def iterativeCalculate(n):
	numbers = []
	for num in str(n):
		numbers.append(int(num))
				
	return sum(numbers)

def recursiveCalculate(n):
	numbers = str(n)
	if (len(numbers) == 0):
		return 0
	
	return int(numbers[0]) + recursiveCalculate(numbers[1:])



