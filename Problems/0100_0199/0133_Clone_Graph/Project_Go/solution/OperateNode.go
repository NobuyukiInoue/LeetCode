package solution

import (
	"strings"
)

func CreateTreeNode(flds string) *Node {
	fldsArr := strings.Split(flds, "],[")
	data := make([][]int, len(fldsArr))
	for i := 0; i < len(data); i++ {
		data[i] = StringToIntArray(fldsArr[i])
	}

	nodes := make([]*Node, len(data))
	for i, _ := range data {
		nodes[i] = &Node{i + 1, nil}
	}
	for i, _ := range nodes {
		tempNodes := make([]*Node, 0)
		for j, _ := range data[i] {
			tempNodes = append(tempNodes, nodes[data[i][j]-1])
		}
		nodes[i].Neighbors = tempNodes
	}
	return nodes[0]
}

func NodeToString(node *Node) string {
	if node == nil {
		return "[]"
	} else if node.Neighbors == nil {
		return "[[]]"
	}
	resultStr := ""
	data := make(map[int][]int, 0)
	for _, nei := range node.Neighbors {
		data[node.Val] = append(data[node.Val], nei.Val)
	}

	for _, nei := range node.Neighbors {
		_, exists := data[nei.Val]
		if !exists {
			for _, nei2 := range nei.Neighbors {
				data[nei.Val] = append(data[nei.Val], nei2.Val)
			}
		}

		for _, nei2 := range nei.Neighbors {
			_, exists := data[nei2.Val]
			if !exists {
				for _, nei3 := range nei2.Neighbors {
					data[nei2.Val] = append(data[nei2.Val], nei3.Val)
				}
			}
		}
	}
	resultStr = ""
	for k, _ := range data {
		if resultStr == "" {
			resultStr += "[" + IntArrayToString(data[k]) + "]"
		} else {
			resultStr += ",[" + IntArrayToString(data[k]) + "]"
		}
	}
	return resultStr
}
