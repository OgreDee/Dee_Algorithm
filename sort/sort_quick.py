# ---------------------快速排序(mergesort)---------------------
# 快速排序
# 算法描述: 选取pivot基准元素(pivot一般是第一个), 把比pivot小的元素移到左侧，大的移到右侧, 然后递归上个步骤。
# 时间复杂度: O(nlogn）
# https://zhuanlan.zhihu.com/p/63202860

print("---------------------快速排序---------------------")
data = [54, 32, 99, 103, 22, 8, 201, 33]

def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def sort_quick(arr, left, right):
	if left >= right:
		return

	start = left
	end = right

	pivot = arr[left]
	while left < right:
		while right > left and data[right] >= pivot:
			right = right - 1
			pass
		swap(data, left, right)

		while left < right and data[left] <= pivot:
			left = left + 1
			pass
		swap(data, left, right)
	
	sort_quick(arr, start, left)
	sort_quick(arr, left + 1, end)



print("排序前: " +','.join(str(i) for i in data))
sort_quick(data, 0, len(data)-1)
print("排序后: " +','.join(str(i) for i in data))