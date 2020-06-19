package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

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

	root := createTreeNode(flds)
	fmt.Printf("root = \n%s", tree2staircaseString(root))
	fmt.Printf("root = %s\n", tree2str(root))

	timeStart := time.Now()
	codec := Constructor()

	root = codec.deserialize(flds)
	result := codec.serialize(root)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
