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

def fourNumberSum_without_ordering(array, targetSum):
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

def fourNumberSum_without_duplicate(arr, X):
	list = [] 
	N = len(array)
	Map = {}
	for i in range(N-1):
		for j in range(i+1, N):
			Map[array[i] + array[j]] = [i, j]
	
	temp = [0 for i in range(N)]

    # Iterate from 0 to length of arr
	for i in range(N - 1):
    
        # Iterate from i + 1 to length of arr
		for j in range(i + 1, N):
             
            # Store curr_sum = arr[i] + arr[j]
			curr_sum = arr[i] + arr[j]
 
            # Check if X - curr_sum if present
            # in map
			if (X - curr_sum) in Map:
                 
                # Store pair having map value
                # X - curr_sum
				p = Map[X - curr_sum]
 
				if (p[0] != i and p[1] != i and
					p[0] != j and p[1] != j and
					temp[p[0]] == 0 and temp[p[1]] == 0 and
					temp[i] == 0 and temp[j] == 0):
                         
                    # Print the output
					print(arr[i], ",", arr[j], ",", arr[p[0]], ",", arr[p[1]], sep = "")
					list.append([arr[i], arr[j], arr[p[0]], arr[p[1]]])
					
					temp[p[0]] = 1          
					temp[p[1]] = 1
					temp[i] = 1
					temp[j] = 1
	return list
                

if __name__ == '__main__':
	#array = [-8, -6, 1, 2, -3, 4, -5, 6, 8, 3, 5]
	#target = 0
	#print(twoNumberSum(array, target))
	#print(threeNumberSum(array, target))
	
	array = [7, 6, 4, -1, 1, 2]
	target = 16
	#print(fourNumberSum(array, target))

	array = [1, 2, 3, 4, 5, 6, 7]
	target = 10
	#print(fourNumberSum(array, target))

	array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
	target = 30
	print(fourNumberSum_without_ordering(array, target))
	print(fourNumberSum_without_duplicate(array, target))

	#Expected o/p
	"""
	[-1, 22, 7, 2],
  	[22, 4, 7, -3],
  	[-1, 18, 11, 2],
  	[18, 4, 11, -3],
  	[22, 11, 2, -5]
	"""


