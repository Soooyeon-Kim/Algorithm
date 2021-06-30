queue = []
tree = [1, 2, 3, 4, 5, 6, 7]

root = 0

queue.append(root)
while len(queue) > 0:
	length = len(queue)
	while length > 0:
		current = queue.pop(0)
		length = length - 1
		print(tree[current])
		left = current * 2 + 1
		right = current * 2 + 2
		if left < len(tree):
			queue.append(left)
		if right < len(tree):
			queue.append(right)