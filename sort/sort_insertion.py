# ---------------------简单插入排序---------------------
# 简单插入排序属于插入排序
# 算法描述: 从第二个元素开始，比前一个元素小，就把前面队列中的元素往后移，找到合适的位置插入进去
# 时间复杂度: O(n^2)
# 数据规模小或者基本有序时，效率高

print("---------------------简单插入排序---------------------")

data = [54, 32, 99, 103, 22, 8, 201, 33]

def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def sort_insertion():
	for count in range(1, len(data)):
		v = data[count]
		index = count - 1
		while index >= 0 and data[index] > v:
			data[index + 1] = data[index]
			index = index - 1
			pass
		data[index+1] = v


print("排序前: " +','.join(str(i) for i in data))
sort_insertion()
print("排序后: " +','.join(str(i) for i in data))