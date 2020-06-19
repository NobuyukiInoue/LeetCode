package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func createNode(flds string) *Node {
	return createSubNode(strings.Split(flds, ","), 0, 0)
}

func createSubNode(flds []string, depth int, pos int) *Node {
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

	val, err := strconv.Atoi(flds[curPos+pos])

	if err != nil {
		fmt.Printf("setNode() Error ... flds[%d] = %s", curPos+pos, flds[curPos+pos])
		return nil
	}

	node := new(Node)
	node.Val = val
	node.Left = createSubNode(flds, depth+1, 2*pos)
	node.Right = createSubNode(flds, depth+1, 2*pos+1)
	return node
}

var resultList = []string{}

func TreeToStaircaseString(node *Node) string {
	resultList = []string{}

	resultStr := treeToStaircaseSubString(node, 0)
	resultList = nil

	return resultStr
}

func treeToStaircaseSubString(node *Node, n int) string {
	if node == nil {
		return ""
	}

	if len(resultList) <= n {
		resultList = append(resultList, "("+strconv.Itoa(node.Val)+")")
	} else {
		resultList[n] = resultList[n] + ",(" + strconv.Itoa(node.Val) + ")"
	}

	if node.Left != nil {
		treeToStaircaseSubString(node.Left, n+1)
	}
	if node.Right != nil {
		treeToStaircaseSubString(node.Right, n+1)
	}

	resultStr := ""
	for _, s := range resultList {
		resultStr += s + "\n"
	}

	return resultStr
}

func TreeToStaircaseString_with_next(node *Node) string {
	resultList = []string{}

	resultStr := treeToStaircaseSubString_with_next(node, 0)
	resultList = nil

	return resultStr
}

func treeToStaircaseSubString_with_next(node *Node, n int) string {
	if node == nil {
		return ""
	}

	if len(resultList) <= n {
		resultList = append(resultList, "("+strconv.Itoa(node.Val)+")")
	} else {
		resultList[n] = resultList[n] + ",(" + strconv.Itoa(node.Val) + ")"
	}

	if node.Next == nil {
		resultList[n] = resultList[n] + ",(#)"
	}

	if node.Left != nil {
		treeToStaircaseSubString_with_next(node.Left, n+1)
	}
	if node.Right != nil {
		treeToStaircaseSubString_with_next(node.Right, n+1)
	}

	resultStr := ""
	for _, s := range resultList {
		resultStr += s + "\n"
	}

	return resultStr
}

func Tree2str(node *Node) string {
	if node == nil {
		return ""
	}

	resultStr := strconv.Itoa(node.Val)

	if node.Left == nil && node.Right == nil {
		return resultStr
	}

	resultStr += "(" + Tree2str(node.Left) + ")"
	if node.Right != nil {
		resultStr += "(" + Tree2str(node.Right) + ")"
	}

	return resultStr
}
