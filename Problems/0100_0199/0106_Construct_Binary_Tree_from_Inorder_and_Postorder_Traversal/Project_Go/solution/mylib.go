package solution

import (
	"strconv"
	"strings"
	"unsafe"
)

func StringToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func StringToByteArray(flds string) []byte {
	nums := make([]byte, len(flds))

	for i := 0; i < len(nums); i++ {
		nums[i] = (byte)(flds[i])
	}

	return nums
}

func IntArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func IntIntArrayToString(nums [][]int) string {
	if len(nums) <= 0 {
		return "[]"
	}

	resultStr := "[[" + IntArrayToString(nums[0]) + "]"

	for i := 1; i < len(nums); i++ {
		resultStr += ", [" + IntArrayToString(nums[i]) + "]"
	}
	return resultStr + "]"
}

func IntIntArrayToGridString(grid [][]int) string {
	if len(grid) <= 0 {
		return "[[]]"
	}

	resultStr := "[\n"
	resultStr += "  [" + IntArrayToString(grid[0]) + "]\n"
	for i := 1; i < len(grid); i++ {
		resultStr += ", [" + IntArrayToString(grid[i]) + "]" + "\n"
	}
	return resultStr + "]"
}

func ByteByteArrayToString(grid [][]byte) string {
	if len(grid) <= 0 {
		return "[[]]"
	}

	resultStr := "[[" + *(*string)(unsafe.Pointer(&grid[0])) + "]"
	for i := 1; i < len(grid); i++ {
		resultStr += ", [" + *(*string)(unsafe.Pointer(&grid[i])) + "]"
	}
	return resultStr + "]"
}

func ByteByteArrayToGridString(grid [][]byte) string {
	if len(grid) <= 0 {
		return "[[]]"
	}

	resultStr := "[\n"
	resultStr += "  [" + *(*string)(unsafe.Pointer(&grid[0])) + "]\n"
	for i := 1; i < len(grid); i++ {
		resultStr += ", [" + *(*string)(unsafe.Pointer(&grid[i])) + "]\n"
	}
	return resultStr + "]"
}

func StringArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := "\"" + data[0] + "\""
	for i := 1; i < len(data); i++ {
		resultStr += ", \"" + data[i] + "\""
	}

	return resultStr
}

func StringStringArrayToString(data [][]string) string {
	if len(data) <= 0 {
		return "[]"
	}

	res := ""
	for i := 0; i < len(data); i++ {
		res += "[\n"
		for j := 0; j < len(data[i]); j++ {
			if j == 0 {
				res += " [" + data[i][j] + "]\n"
			} else {
				res += ",[" + data[i][j] + "]\n"
			}
		}
		res += "]\n"
	}

	return res
}
