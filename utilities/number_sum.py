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
	for i in range(len(array) - 3):
		left = i + 1
		right = len(array) - 1
		while left < right:
			inner = left + 1
			while inner < right: 
				currentSum = array[i] + array[left] + array[inner] + array[right]
				if currentSum == targetSum:
					list.append([array[i], array[left], array[inner], array[right]])
				inner += 1
			right -= 1
	return list

if __name__ == '__main__':
	array = [-8, -6, 1, 2, -3, 4, -5, 6, 8, 3, 5]
	target = 0
	print(twoNumberSum(array, target))
	print(threeNumberSum(array, target))
	print(fourNumberSum(array, target))