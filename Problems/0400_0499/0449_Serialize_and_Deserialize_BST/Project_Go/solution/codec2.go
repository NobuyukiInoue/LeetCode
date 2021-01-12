package solution

import (
	"math"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
/*
 The tree can be built using preorder or postorder traversal and inorder traversal.
 since the tree is BST, we already know that inorder traversal can give sorted order.
serialize tree using preorder or postorder traversal
deserialize using preoder/postorder and inorder traversal
*/

// 148ms

type Codec2 struct {

}

func Constructor() Codec2 {
	return Codec2{}
}

// Serializes a tree to a single string.
func (this *Codec2) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}

	nodes := []rune{}
	var preOrder func(*TreeNode)
	preOrder = func(curr *TreeNode) {
		if curr == nil {
			return
		}
		nodes = append(nodes, rune(curr.Val))
		preOrder(curr.Left)
		preOrder(curr.Right)
	}

	preOrder(root)
	return string(nodes)
}


// Deserializes your encoded data to tree.
func (this *Codec2) deserialize(data string) *TreeNode {
	if len(data) == 0 {
		return nil
	}
	nodes := []rune{}
	for _, n := range data {
		nodes = append(nodes, n)
	}
	var buildTree func([]rune, int, int) *TreeNode
	startIndex := 0
	buildTree = func(nodes []rune, min, max int) *TreeNode {
		if startIndex == len(nodes) {
			return nil
		}
		val := int(nodes[startIndex])
		if val < min || val > max{
			return nil
		}
		root := &TreeNode{val, nil, nil}
		startIndex++
		root.Left = buildTree(nodes, min, val)
		root.Right = buildTree(nodes,val, max)
		return root
	}
	return buildTree(nodes, math.MinInt32, math.MaxInt32)
}


/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * data := obj.serialize(root);
 * ans := obj.deserialize(data);
 */
 