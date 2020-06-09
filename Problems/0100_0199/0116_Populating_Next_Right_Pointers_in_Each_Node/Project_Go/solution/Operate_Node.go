package solution

import (
	"fmt"
	"math"
	"strconv"
)

func setNode(flds []string) *Node {
	return setNode2(flds, 0, 0)
}

func setNode2(flds []string, depth int, pos int) *Node {
	if len(flds) == 0 {
		return nil
	}

	curPos := 0
	for i := 0; i < depth; i++ {
		curPos += int(math.Pow(2.0, float64(i)))
	}

	if curPos+pos > len(flds)-1 {
		return nil
	}

	if flds[curPos+pos] == "null" {
		return nil
	}

	node := new(Node)
	val, err := strconv.Atoi(flds[curPos+pos])

	if err != nil {
		fmt.Printf("setNode() Error ... flds[%d] = %s", curPos+pos, flds[curPos+pos])
		return nil
	}

	node.Val = val
	node.Left = setNode2(flds, depth+1, 2*pos)
	node.Right = setNode2(flds, depth+1, 2*pos+1)

	return node
}

var resultStr = []string{}

func outputNode(node *Node) string {
	resultStr = []string{}

	outStr := setResultStr(node, 0)
	resultStr = nil

	return outStr
}

func setResultStr(node *Node, n int) string {
	if node == nil {
		return ""
	}

	if len(resultStr) <= n {
		resultStr = append(resultStr, "("+strconv.Itoa(node.Val)+")")
	} else {
		resultStr[n] = resultStr[n] + ",(" + strconv.Itoa(node.Val) + ")"
	}

	if node.Left != nil {
		setResultStr(node.Left, n+1)
	}
	if node.Right != nil {
		setResultStr(node.Right, n+1)
	}

	outputStr := ""
	for _, s := range resultStr {
		outputStr += s + "\n"
	}

	return outputStr
}

func outputNode_with_next(node *Node) string {
	resultStr = []string{}

	outStr := setResultStr_with_next(node, 0)
	resultStr = nil

	return outStr
}

func setResultStr_with_next(node *Node, n int) string {
	if node == nil {
		return ""
	}

	if len(resultStr) <= n {
		resultStr = append(resultStr, "("+strconv.Itoa(node.Val)+")")
	} else {
		resultStr[n] = resultStr[n] + ",(" + strconv.Itoa(node.Val) + ")"
	}

	if node.Next == nil {
		resultStr[n] = resultStr[n] + ",(#)"
	}

	if node.Left != nil {
		setResultStr_with_next(node.Left, n+1)
	}
	if node.Right != nil {
		setResultStr_with_next(node.Right, n+1)
	}

	outputStr := ""
	for _, s := range resultStr {
		outputStr += s + "\n"
	}

	return outputStr
}

func Tree2str(t *Node) string {
	if t == nil {
		return ""
	}

	resultStr := strconv.Itoa(t.Val)

	if t.Left == nil && t.Right == nil {
		return resultStr
	}

	resultStr += "(" + Tree2str(t.Left) + ")"
	if t.Right != nil {
		resultStr += "(" + Tree2str(t.Right) + ")"
	}

	return resultStr
}
