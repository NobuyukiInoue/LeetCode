package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	if sr < len(image) && sc < len(image[sr]) && image[sr][sc] != newColor {
		helper(image, sr, sc, image[sr][sc], newColor)
	}

	return image
}

func helper(image [][]int, i int, j int, comp int, newColor int) {
	if 0 <= i && i < len(image) && 0 <= j && j < len(image[i]) {
		if image[i][j] == comp {
			image[i][j] = newColor
			helper(image, i-1, j, comp, newColor)
			helper(image, i, j-1, comp, newColor)
			helper(image, i+1, j, comp, newColor)
			helper(image, i, j+1, comp, newColor)
		}
	}
}

func IntArray2string(arr [][]int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i == 0 {
			resultStr += "["
		} else {
			resultStr += ",["
		}
		for j := 0; j < len(arr[i]); j++ {
			if j > 0 {
				resultStr += ","
			}
			resultStr += strconv.Itoa(arr[i][j])
		}
		resultStr += "]"
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)

	flds := strings.Split(temp, "]],[")

	arr1 := strings.Split(flds[0], "],[")
	arr2_temp := strings.Replace(flds[1], "]]", "", -1)
	arr2 := strings.Split(arr2_temp, "],[")

	image := make([][]int, len(arr1))
	for i := 0; i < len(arr1); i++ {
		image[i] = make([]int, 3)
		arr1_temp := strings.Split(arr1[i], ",")
		for j := 0; j < len(arr1_temp); j++ {
			image_temp, _ := strconv.Atoi(arr1_temp[j])
			image[i][j] = image_temp
		}
	}

	sr, _ := strconv.Atoi(arr2[0])
	sc, _ := strconv.Atoi(arr2[1])
	newColor, _ := strconv.Atoi(arr2[2])

	fmt.Printf("image[] = %s\n", IntArray2string(image))
	fmt.Printf("sr = %d, sc = %d, newColor = %d\n", sr, sc, newColor)

	timeStart := time.Now()

	result := floodFill(image, sr, sc, newColor)
	fmt.Printf("result = %s\n", IntArray2string(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
