# ---------------------简单选择排序---------------------
# 简单选择排序属于选择排序
# 算法描述: 选择最大的元素和队尾交换，再从剩下的数据中重复上个步骤
# 时间复杂度: O(n^2)

print("---------------------简单选择排序---------------------")

data = [54, 32, 99, 103, 22, 8, 201, 33]

def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def sort_selection():
	for count in range(len(data), 1, -1):
		minIndex = 0
		for index in range(count):
			if data[index] > data[minIndex]:
				minIndex = index

		swap(data, count - 1, minIndex)


print("排序前: " +','.join(str(i) for i in data))
sort_selection()
print("排序后: " +','.join(str(i) for i in data))