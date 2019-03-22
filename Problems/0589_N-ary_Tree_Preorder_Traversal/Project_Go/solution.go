package main

import (
	//	"encoding/json"
	"encoding/json"
	"fmt"
	"strconv"
	"strings"

	//	"strings"
	"time"
)

func Preorder(root *Node) []int {
	result := make([]int, 0)

	if root == nil {
		return result
	}

	result = append(result, root.val)

	if root.children == nil {
		return result
	}

	for _, node := range *root.children {
		tempList := Preorder(&node)
		for _, tempVal := range tempList {
			result = append(result, tempVal)
		}
	}

	return result
}

func IntArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "$id", "val", -1)
	jsonText := []byte(temp)

	var root *Node
	json.Unmarshal(jsonText, &root)
	//	root = SetSampleNode()

	fmt.Printf("root = \n%s\n", OutputNode(root))

	timeStart := time.Now()

	result := Preorder(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArray2string(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
