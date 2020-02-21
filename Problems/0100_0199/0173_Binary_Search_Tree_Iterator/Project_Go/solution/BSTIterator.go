package solution

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// 40ms

var nums []int

type BSTIterator struct {
	index int
	nums  []int
}

func Constructor(root *TreeNode) BSTIterator {
	nums = make([]int, 0)
	dfs(root)

	BI := new(BSTIterator)
	BI.index = 0
	BI.nums = nums

	return *BI
}

func dfs(node *TreeNode) {
	if node == nil {
		return
	}
	if node.Left != nil {
		dfs(node.Left)
	}
	nums = append(nums, node.Val)
	if node.Right != nil {
		dfs(node.Right)
	}
}

/** @return the next smallest number */
func (this *BSTIterator) Next() int {
	if this.index < len(this.nums) {
		this.index++
		return this.nums[this.index-1]
	}
	return -1
}

/** @return whether we have a next smallest number */
func (this *BSTIterator) HasNext() bool {
	if this.index < len(this.nums) {
		return true
	}
	return false
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
