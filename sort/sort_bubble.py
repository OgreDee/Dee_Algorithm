# ---------------------冒泡排序---------------------
# 冒泡排序属于交换排序
# 越小的元素会经由交换慢慢“浮”到数列的顶端所以叫做冒泡排序
# 算法描述: 两两交换，如果比后面的元素大就交换位置
# 时间复杂度: O(n^2)

print("---------------------冒泡排序---------------------")

data = [54, 32, 99, 103, 22, 8, 201, 33]

def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def sort_bubble():
	for index in range(len(data) - 1):
		for index in range(len(data) - 1):
			if data[index] > data[index+1]:
				swap(data, index, index + 1)


print("排序前: " +','.join(str(i) for i in data))
sort_bubble()
print("排序后: " +' - '.join(str(i) for i in data))
