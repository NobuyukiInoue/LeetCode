package solution

import (
	//	"encoding/json"

	"fmt"

	//	"strings"
	"time"
)

var result []int

func PostOrder(root *Node) []int {
	if root != nil {
		if root.children != nil {
			for _, node := range *root.children {
				PostOrder(&node)
			}
		}
		result = append(result, root.val)
	}
	return result
}

func LoopMain(args string) {
	//	temp := strings.Trim(args, "")
	//	temp = strings.Replace(temp, "$id", "val", -1)
	//	jsonText := []byte(temp)

	//	var root Node
	//	json.Unmarshal(jsonText, &root)
	root := SetSampleNode()

	fmt.Printf("root = \n%s\n", OutputNode(root))

	timeStart := time.Now()

	result := make([]int, 0)
	result = PostOrder(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
