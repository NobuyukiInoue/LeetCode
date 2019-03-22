package main

import "strconv"

func SetSampleNode() *Node {
	n1_list := make([]Node, 0)
	n1_list = append(n1_list, *NewNode(5, nil))
	n1_list = append(n1_list, *NewNode(6, nil))

	n0_list := make([]Node, 0)
	n0_list = append(n0_list, *NewNode(3, &n1_list))
	n0_list = append(n0_list, *NewNode(2, nil))
	n0_list = append(n0_list, *NewNode(4, nil))

	node := NewNode(1, &n0_list)

	return node
}

var resultStr []string

func OutputNode(node *Node) string {
	if node == nil {
		return ""
	}

	resultStr = make([]string, 0)
	resultStr = append(resultStr, strconv.Itoa(node.val))
	//resultList = append(resultList, node.val)
	SetOutputNode(node, 1)

	if len(resultStr) <= 0 {
		return ""
	}

	result := "[\n"

	for i, _ := range resultStr {
		if resultStr[i] == "" {
			break
		}

		if i < len(resultStr)-1 {
			result += "\t[" + resultStr[i] + "],\n"
		} else {
			result += "\t[" + resultStr[i] + "]\n"
		}
	}

	result += "]"

	//	resultStr = make([]string, 0)
	return result
}

func SetOutputNode(node *Node, n int) {
	if node == nil {
		return
	}

	if node.children == nil {
		return
	}

	tempStr := ""

	for i := 0; i < len(*node.children); i++ {
		if i == 0 {
			tempStr += strconv.Itoa((*node.children)[i].val)
			//tempStr += (*node.children)[i].val
		} else {
			tempStr += "," + strconv.Itoa((*node.children)[i].val)
			//tempStr += "," + (*node.children)[i].val
		}
	}

	if len(resultStr) <= n {
		resultStr = append(resultStr, tempStr)
	} else {
		resultStr[n] += tempStr
	}

	for i := 0; i < len(*node.children); i++ {
		SetOutputNode(&(*node.children)[i], n+1)
	}
}
