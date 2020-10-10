# ---------------------归并排序(mergesort)---------------------
# 归并排序
# 算法描述: 归并排序（MERGE-SORT）是利用归并的思想实现的排序方法，该算法采用经典的分治（divide-and-conquer）策略（分治法将问题分(divide)成一些小的问题然后递归求解，而治(conquer)的阶段则将分的阶段得到的各答案"修补"在一起，即分而治之)。
# 时间复杂度: O(nlogn）

print("---------------------归并排序---------------------")

data = [54, 32, 99, 103, 60, 22, 8, 201, 33]

#治
def merge(arr, temp, left, mid, right):
	print("merge: " , left, mid, right)

	lp = left
	rp = mid+1
	i = 0
	while lp <= mid and rp <= right:
		if arr[lp] < arr[rp]:
			temp[i] = arr[lp]
			i = i + 1
			lp = lp + 1
		else:
			temp[i] = arr[rp]
			i = i + 1
			rp = rp + 1

	while lp <= mid:
		temp[i] = arr[lp]
		i = i + 1
		lp = lp + 1

	while rp <= right:
		temp[i] = arr[rp]
		i = i + 1
		rp = rp + 1


	#拷贝
	i = 0
	while left <= right:
		arr[left] = temp[i]
		left = left + 1
		i = i + 1
		pass
	

#分
def divide(arr, temp, left, right):
	if(left < right):
		print(left, right)
		mid = int((right + left) / 2)
		divide(arr, temp, left, mid)
		divide(arr, temp, mid + 1, right)

		merge(arr, temp, left, mid, right)

	pass


def sort_merge():
	temp = [0 for i in range(len(data))]
	divide(data, temp, 0, len(data) - 1)
	pass

print("排序前: " +','.join(str(i) for i in data))
sort_merge()
print("排序后: " +','.join(str(i) for i in data))