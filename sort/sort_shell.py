# ---------------------希尔排序(shellsort)---------------------
# 希尔排序属于插入排序
# 算法描述: 首先它把较大的数据集合分割成若干个小组（逻辑上分组），然后对每一个小组分别进行插入排序, 分组第一组t1(len/2)....tn(1)
# 时间复杂度: 未知
import math

print("---------------------希尔排序---------------------")

data = [54, 32, 99, 103, 60, 22, 8, 201, 33]

def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def sort_insertion(l, startIdx, gap):
	for count in range(startIdx + gap, len(l), gap):
		v = l[count]
		index = count - gap
		while index >= 0 and l[index] > v:
			l[index + gap] = l[index]
			index = index - gap
			pass
		l[index+gap] = v


def sort_shell():
	_len = len(data)
	gap = math.floor(_len / 2)
	while gap > 0:
		for startIdx in range(0,gap):
			sort_insertion(data, startIdx, gap)
			pass
		gap = math.floor(gap / 2)
	pass


print("排序前: " +','.join(str(i) for i in data))
sort_shell()
print("排序后: " +','.join(str(i) for i in data))
