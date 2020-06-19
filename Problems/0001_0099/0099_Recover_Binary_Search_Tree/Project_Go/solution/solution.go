package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

/*
var firstElement *TreeNode
var secondElement *TreeNode
var prevElement *TreeNode

func recoverTree(root *TreeNode) {
	traverse(root)
	temp := firstElement.Val
	firstElement.Val = secondElement.Val
	secondElement.Val = temp
}

func traverse(root *TreeNode) {
	if root == nil {
		return
	}
	traverse(root.Left)
	if prevElement != nil {
		if root.Val <= prevElement.Val {
			if firstElement == nil {
				firstElement = prevElement
				secondElement = root
			} else {
				secondElement = root
			}
		}
	}
	prevElement = root
	traverse(root.Right)
}
*/

func recoverTree(root *TreeNode) {
	stack := make([]*TreeNode, 0)
	var prev *TreeNode
	var firstStartPointer *TreeNode
	var lastEndPointer *TreeNode
	cur := root
	for len(stack) != 0 || cur != nil {
		if cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			temp := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if prev != nil && prev.Val > temp.Val {
				if firstStartPointer == nil {
					firstStartPointer = prev
				}
				lastEndPointer = temp
			}
			prev = temp

			if temp.Right != nil {
				cur = temp.Right
			}
		}

	}
	firstStartPointer.Val, lastEndPointer.Val = lastEndPointer.Val, firstStartPointer.Val
}

func LoopMain(args string) {
	// コメント部の削除
	rep := regexp.MustCompile("#.*")
	args = rep.ReplaceAllString(args, "")
	rep = regexp.MustCompile("//.*")
	args = rep.ReplaceAllString(args, "")
	if len(args) == 0 {
		return
	}

	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := CreateTreeNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	recoverTree(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(root))
	fmt.Printf("result = %s\n", Tree2str(root))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
