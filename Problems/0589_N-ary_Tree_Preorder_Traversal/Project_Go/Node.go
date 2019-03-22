package main

type Node struct {
	val      int     `json:"val"`
	children *[]Node `json:"children"`
}

func NewNode(new_val int, new_children *[]Node) *Node {
	node := new(Node)
	node.val = new_val
	node.children = new_children
	return node
}
