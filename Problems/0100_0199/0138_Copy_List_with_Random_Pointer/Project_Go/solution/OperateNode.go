package solution

import (
	"strconv"
	"strings"
)

func CreateNode(flds []string) *Node {
	nodes := make([]*Node, 0)
	for _, fld := range flds {
		temp := strings.Split(fld, ",")
		val, _ := strconv.Atoi(temp[0])
		nodes = append(nodes, &Node{val, nil, nil})
	}
	head := nodes[0]
	cur := head
	for i := 0; ; i++ {
		temp := strings.Split(flds[i], ",")
		if temp[1] != "null" {
			random, _ := strconv.Atoi(temp[1])
			cur.Random = nodes[random]
		}
		if i == len(nodes)-1 {
			break
		}
		cur.Next = nodes[i+1]
		cur = cur.Next
	}
	return head
}

func NodeToString(head *Node) string {
	result := IntIntArrayToString(NodeToStringArray(head))
	return strings.Replace(result, "-1", "null", -1)
}

func NodeToStringArray(head *Node) [][]int {
	nodes := make([]*Node, 0)
	cur := head
	for cur != nil {
		nodes = append(nodes, cur)
		cur = cur.Next
	}
	flds := make([][]int, 0)
	cur = head
	for cur != nil {
		flds = append(flds, []int{cur.Val, findNodeIndex(nodes, cur.Random)})
		cur = cur.Next
	}
	return flds
}

func findNodeIndex(nodes []*Node, target *Node) int {
	if target == nil {
		return -1
	}
	for i, node := range nodes {
		if target == node {
			return i
		}
	}
	return -1
}
