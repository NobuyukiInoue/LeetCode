package solution

import (
	"fmt"
	"strings"
	"time"
)

func rotateTheBox(box [][]byte) [][]byte {
	// 406ms - 444ms
	m, n := len(box), len(box[0])
	res := make([][]byte, n)
	for i, _ := range res {
		res[i] = make([]byte, m)
	}
	for i := 0; i < m; i++ {
		k := n - 1
		for j := n - 1; j >= 0; j-- {
			res[j][m-i-1] = '.'
			if box[i][j] != '.' {
				if box[i][j] == '*' {
					k = j
				}
				res[k][m-i-1] = box[i][j]
				k--
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	box := make([][]byte, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		box[i] = StringToByteArray(str_mat[i])
	}
	fmt.Printf("box = %s\n", ByteByteArrayToGridString(box))

	timeStart := time.Now()

	result := rotateTheBox(box)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("result = %s\n", ByteByteArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
