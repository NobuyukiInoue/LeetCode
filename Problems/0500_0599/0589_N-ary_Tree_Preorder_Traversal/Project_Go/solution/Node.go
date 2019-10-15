package solution

type Node struct {
	val      int     `json:"val,string"`
	children *[]Node `json:"children,string"`
}

func NewNode(new_val int, new_children *[]Node) *Node {
	node := new(Node)
	node.val = new_val
	node.children = new_children
	return node
}
