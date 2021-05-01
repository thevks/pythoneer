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

def fourNumberSum(array, targetSum):
	array.sort()
	list = []
	left = 0
	right = len(array) - 1
	while left < right :
		inner_left = left + 1
		inner_right = right - 1
		partial_sum = targetSum - (array[left] + array[right])
		while inner_left < inner_right :
			current_sum = array[inner_left] + array[inner_right]
			if current_sum == partial_sum :
				list.append([array[left], array[inner_left], array[inner_right], array[right]])
				inner_left += 1
				inner_right -= 1
			elif current_sum < partial_sum :
				inner_left += 1
			else:
				inner_right -= 1
		if (array[left+1] + array[right-1]) < partial_sum:
			left += 1
		else:
			right -= 1
	return list

if __name__ == '__main__':
	#array = [-8, -6, 1, 2, -3, 4, -5, 6, 8, 3, 5]
	#target = 0
	#print(twoNumberSum(array, target))
	#print(threeNumberSum(array, target))
	
	array = [7, 6, 4, -1, 1, 2]
	target = 16
	print(fourNumberSum(array, target))

	array = [1, 2, 3, 4, 5, 6, 7]
	target = 10
	print(fourNumberSum(array, target))
