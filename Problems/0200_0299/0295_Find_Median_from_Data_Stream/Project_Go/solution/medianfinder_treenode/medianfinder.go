package medianfinder

type MedianFinder struct {
	root *TreeNode
}

type TreeNode struct {
	val, count, total int

	left, right *TreeNode
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	return MedianFinder{}
}

func (this *MedianFinder) AddNum(num int) {
	if this.root == nil {
		this.root = &TreeNode{val: num, count: 1, total: 1}
	} else {
		add(this.root, num)
	}
}

func add(node *TreeNode, val int) {
	if node.val == val {
		node.count++
	} else if node.val > val {
		if node.left == nil {
			node.left = &TreeNode{val: val}
		}
		add(node.left, val)
	} else {
		if node.right == nil {
			node.right = &TreeNode{val: val}
		}
		add(node.right, val)
	}
	node.total++
}

func (this *MedianFinder) FindMedian() float64 {
	if total(this.root)&1 == 0 {
		// elements number is even
		smaller, _ := this.find(total(this.root)/2 - 1)
		larger, _ := this.find(total(this.root) / 2)
		return float64(smaller+larger) / 2
	} else {
		// elements number is odd
		val, _ := this.find(total(this.root) / 2)
		return float64(val)
	}
}

func (t *MedianFinder) find(i int) (val int, found bool) {
	val, found = findWithRoot(t.root, i)
	return
}

func findWithRoot(root *TreeNode, i int) (val int, found bool) {
	if i < 0 || i >= root.total {
		return 0, false
	}

	leftCount := total(root.left)
	if leftCount > i {
		return findWithRoot(root.left, i)
	}

	current := leftCount + root.count
	if current > i {
		return root.val, true
	}

	return findWithRoot(root.right, i-current)
}

func total(tree *TreeNode) int {
	if tree != nil {
		return tree.total
	} else {
		return 0
	}
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
