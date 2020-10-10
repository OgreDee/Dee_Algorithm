# ---------------------堆排序---------------------
# 堆排序属于选择排序
# 时间复杂度: O(nlogn)
# 算法描述: 1.创建堆(完全二叉树, 最大堆用于升序/最小堆用于降序) 2.将堆顶元素与末尾元素进行交换
# https://www.cnblogs.com/chengxiao/p/6129630.html
# https://zhuanlan.zhihu.com/p/45725214(这个代码是错误的)

print("---------------------堆排序---------------------")
data = [54, 32, 54,99, 103, 22, 8, 201, 33]


def swap(list, index0, index1):
	tmp = list[index0]
	list[index0] = list[index1]
	list[index1] = tmp
	pass

def adjustment(heap, startIdx, endIdx):
	tmp = heap[startIdx]

	#左子节点
	idx = startIdx*2+1
	while idx <= endIdx:
		if (idx + 1 < endIdx) and heap[idx] < heap[idx+1]:
			idx = idx+1
		
		if heap[idx] > tmp:
			heap[startIdx] = heap[idx]
			startIdx = idx
		else:
			break

		idx = idx*2+1

	heap[startIdx] = tmp


#创建堆
def buildHeap(list):
	endIdx = len(list) -1
	for idx in range(endIdx, -1, -1):
		adjustment(list, idx, endIdx)
		pass
	pass

def sort_heap(list):
	#创建堆
	buildHeap(list)

	#排序堆
	endIdx = len(list)-1
	for idx in range(endIdx - 1, -1, -1):
		swap(list, 0, idx+1)
		adjustment(list,0, idx)
	pass


print("排序前: " +','.join(str(i) for i in data))
sort_heap(data)
print("排序后: " +','.join(str(i) for i in data))