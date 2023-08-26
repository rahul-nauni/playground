class MergeSort:
	def split(self, arr):
		if len(arr) > 1:
			# split
			left_arr = arr[:len(arr) // 2]
			right_arr = arr[len(arr) // 2:]

			self.split(left_arr)
			self.split(right_arr)

			# merge
			self.merge(arr, left_arr, right_arr)
	
	def merge(self, arr, left_arr, right_arr):
		i = 0
		j = 0
		k = 0

		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		while i < len(left_arr): # elements left in left array
			arr[k] = left_arr[i]
			i += 1
			k += 1
		
		while j <  len(right_arr): # elements left in right array
			arr[k] = right_arr[j]
			j += 1
			k += 1

	def merge_sort(self, arr):
		self.split(arr)
		return arr

arr = [2, 4, 3, 7, 6, 1, 5]
mergeSort = MergeSort()
print(mergeSort.merge_sort(arr))
