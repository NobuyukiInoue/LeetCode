package solution

import (
	"fmt"
	"strings"
	"time"
)

func cloneGraph(node *Node) *Node {
	// 0ms
	if node == nil {
		return nil
	}
	queue := make([]*Node, 0)
	queue = append(queue, node)
	mymap := make(map[*Node]*Node, 0)
	mymap[node] = &Node{node.Val, nil}
	for len(queue) > 0 {
		temp := queue[0]
		queue = queue[1:]
		for _, nei := range temp.Neighbors {
			_, exists := mymap[nei]
			if !exists {
				mymap[nei] = &Node{nei.Val, nil}
				queue = append(queue, nei)
			}
			mymap[temp].Neighbors = append(mymap[temp].Neighbors, mymap[nei])
		}
	}
	return mymap[node]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	var node *Node
	if flds == "" {
		node = &Node{0, nil}
	} else if flds == "[]" {
		node = &Node{0, nil}
	} else {
		node = CreateTreeNode(flds)
	}
	fmt.Printf("node = %s\n", NodeToString(node))

	timeStart := time.Now()

	result := cloneGraph(node)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", NodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
