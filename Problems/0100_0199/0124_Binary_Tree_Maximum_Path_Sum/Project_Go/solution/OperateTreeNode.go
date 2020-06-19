package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func CreateTreeNode(flds string) *TreeNode {
	return createSubTreeNode(strings.Split(flds, ","), 0, 0)
}

func createSubTreeNode(flds []string, depth int, pos int) *TreeNode {
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
		fmt.Printf("createTreeNode() Error ... flds[%d] = %s\n", curPos+pos, flds[curPos+pos])
		return nil
	}

	/*
		node := new(TreeNode)
		node.Val = val
		node.Left = createSubTreeNode(flds, depth+1, 2*pos)
		node.Right = createSubTreeNode(flds, depth+1, 2*pos+1)
	*/
	node := &TreeNode{val, createSubTreeNode(flds, depth+1, 2*pos), createSubTreeNode(flds, depth+1, 2*pos+1)}
	return node
}

var resultList []string

func TreeToStaircaseString(node *TreeNode) string {
	resultList = []string{}
	outStr := TreeToStaircaseSubString(node, 0)
	resultList = nil

	return outStr
}

func TreeToStaircaseSubString(node *TreeNode, n int) string {
	if node == nil {
		return ""
	}

	if len(resultList) <= n {
		resultList = append(resultList, "("+strconv.Itoa(node.Val)+")")
	} else {
		resultList[n] = resultList[n] + ",(" + strconv.Itoa(node.Val) + ")"
	}

	if node.Left != nil {
		TreeToStaircaseSubString(node.Left, n+1)
	}
	if node.Right != nil {
		TreeToStaircaseSubString(node.Right, n+1)
	}

	resultStr := ""
	for _, s := range resultList {
		resultStr += s + "\n"
	}

	return resultStr
}

func Tree2str(node *TreeNode) string {
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
