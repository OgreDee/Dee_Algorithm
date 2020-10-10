# ---------------------计数排序---------------------
# 计数排序属于桶排序
# 时间复杂度: O(n+k) 空间复杂度O(n+k)

print("---------------------计数排序---------------------")

data = [54, 32, 8, 54, 8, 99, 103, 22, 8, 201, 33]

def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def sort_counting():
	bucket = [0 for i in range(201+1)]
	for x in data:
		bucket[x] = bucket[x] + 1
		pass
	i = 0
	for idx in range(0, len(bucket)):
		for x in range(0, bucket[idx]):
			data[i] = idx
			i = i+1


print("排序前: " +','.join(str(i) for i in data))
sort_counting()
print("排序后: " +','.join(str(i) for i in data))