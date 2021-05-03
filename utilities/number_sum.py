def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	list = []
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			list.append([array[left], array[right]])
			left += 1
			right -= 1
		elif currentSum < targetSum:
			left += 1
		else:
			right -= 1
	return list

def threeNumberSum(array, targetSum):
	array.sort()
	list = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				list.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			else:
				right -= 1
	return list

def fourNumberSum_v1(array, targetSum):
	array.sort()
	list = []
	n = len(array)
	for i in range(n-3):
		for j in range(i+1, n-2):
			l = j + 1
			r = n - 1
			while l < r :
				current_sum = array[i] + array[j] + array[l] + array[r]
				if current_sum == targetSum :
					list.append([array[i], array[j], array[l], array[r]])
					l += 1
					r -= 1
				elif current_sum < targetSum :
					l += 1
				else:
					r -= 1
	return list


def fourNumberSum_v2(array, targetSum):
    seen = {}
    result = [] # quadruplets

    # get Q(current pair of numbers) and check if P we have seen P
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum

            if difference in seen:
                for pair in seen[difference]:
                    result.append(pair + [array[i], array[j]])
        
        # Add P(pair of numbers previously seen)
        for k in range(i):
            currentSum = array[k] + array[i]
            if currentSum not in seen:
                seen[currentSum] = []
            seen[currentSum].append([array[k], array[i]])
        
    return result
                

if __name__ == '__main__':
	
	array = [-8, -6, 1, 2, -3, 4, -5, 6, 8, 3, 5]
	target = 0
	print(twoNumberSum(array, target))
	print(threeNumberSum(array, target))

	array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
	target = 30
	print(fourNumberSum_v1(array, target))
	print(fourNumberSum_v2(array, target))

	#Expected o/p
	"""
	[-1, 22, 7, 2],
  	[22, 4, 7, -3],
  	[-1, 18, 11, 2],
  	[18, 4, 11, -3],
  	[22, 11, 2, -5]
	"""
