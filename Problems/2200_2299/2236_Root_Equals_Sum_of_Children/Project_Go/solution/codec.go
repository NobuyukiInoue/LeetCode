package solution

import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// 204ms

type Codec struct {
	nodesStr []string
}

func Constructor() Codec {
	return Codec{[]string{}}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	this.nodesStr = make([]string, 0)
	this.buildString(root)
	return strings.Join(this.nodesStr, ",")
}

func (this *Codec) buildString(root *TreeNode) {
	if root == nil {
		this.nodesStr = append(this.nodesStr, "null")
	} else {
		this.nodesStr = append(this.nodesStr, strconv.Itoa(root.Val))
		this.buildString(root.Left)
		this.buildString(root.Right)
	}
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	this.nodesStr = strings.Split(data, ",")
	return this.buildTree()
}

func (this *Codec) buildTree() *TreeNode {
	if len(this.nodesStr) > 0 && (this.nodesStr)[0] == "null" {
		return nil
	}
	if len(this.nodesStr) <= 0 {
		return nil
	}
	data, _ := strconv.Atoi((this.nodesStr)[0])
	node := TreeNode{data, nil, nil}
	if len(this.nodesStr) > 1 {
		this.nodesStr = this.nodesStr[1:]
	} else {
		this.nodesStr = []string{}
	}
	node.Left = this.buildTree()

	if len(this.nodesStr) > 1 {
		this.nodesStr = this.nodesStr[1:]
	} else {
		this.nodesStr = []string{}
	}
	node.Right = this.buildTree()
	return &node
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * data := obj.serialize(root);
 * ans := obj.deserialize(data);
 */
