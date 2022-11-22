package solution

import (
	"fmt"
	"strconv"
	"strings"
)

func createListNestedInteger(flds_str string) []*NestedInteger {
	var ni []*NestedInteger
	for len(flds_str) > 0 {
		//	fmt.Printf("flds_str = %s\n", flds_str)
		if flds_str[0] == '[' {
			end_pos, depth := 1, 1
			for depth > 0 && end_pos < len(flds_str) {
				if flds_str[end_pos] == '[' {
					depth++
				} else if flds_str[end_pos] == ']' {
					depth--
				}
				end_pos++
			}
			substr := flds_str[1 : end_pos-1]
			ni = append(ni, createNestedInteger(substr))
			if end_pos < len(flds_str)-1 {
				flds_str = flds_str[end_pos+1:]
			} else {
				flds_str = ""
			}
		} else {
			pos1 := strings.Index(flds_str, ",")
			pos2 := strings.Index(flds_str, "]")
			if pos1 == -1 && pos2 == -1 {
				val, _ := strconv.Atoi(flds_str)
				ni = append(ni, &NestedInteger{&val, nil})
				flds_str = ""
			} else if pos2 >= 0 {
				var pos int
				if pos2 < pos1 || pos1 == -1 {
					pos = pos2
				} else {
					pos = pos1
				}
				val, _ := strconv.Atoi(flds_str[:pos])
				ni = append(ni, &NestedInteger{&val, nil})
				flds_str = flds_str[pos+1:]
			} else if pos1 >= 0 {
				val, _ := strconv.Atoi(flds_str[:pos1])
				ni = append(ni, &NestedInteger{&val, nil})
				flds_str = flds_str[pos1+1:]
			} else {
				fmt.Printf("createNestedInteger() Error.\n")
			}
		}
	}
	return ni
}

func createNestedInteger(flds_str string) *NestedInteger {
	var ni NestedInteger
	for len(flds_str) > 0 {
		//	fmt.Printf("flds_str = %s\n", flds_str)
		if flds_str[0] == '[' {
			end_pos, depth := 1, 1
			for depth > 0 && end_pos < len(flds_str) {
				if flds_str[end_pos] == '[' {
					depth++
				} else if flds_str[end_pos] == ']' {
					depth--
				}
				end_pos++
			}
			substr := flds_str[1 : end_pos-1]
			ni.Add(*createNestedInteger(substr))
			if end_pos < len(flds_str)-1 {
				flds_str = flds_str[end_pos+1:]
			} else {
				flds_str = ""
			}
		} else {
			pos1 := strings.Index(flds_str, ",")
			pos2 := strings.Index(flds_str, "]")
			if pos1 == -1 && pos2 == -1 {
				val, _ := strconv.Atoi(flds_str)
				ni.Add(NestedInteger{&val, nil})
				flds_str = ""
			} else if pos2 >= 0 {
				var pos int
				if pos2 < pos1 || pos1 == -1 {
					pos = pos2
				} else {
					pos = pos1
				}
				val, _ := strconv.Atoi(flds_str[:pos])
				ni.Add(NestedInteger{&val, nil})
				flds_str = flds_str[pos+1:]

			} else if pos1 >= 0 {
				val, _ := strconv.Atoi(flds_str[:pos1])
				ni.Add(NestedInteger{&val, nil})
				flds_str = flds_str[pos1+1:]
			} else {
				fmt.Printf("createNestedInteger() Error.\n")
			}
		}
	}
	return &ni
}

func listNestedIntegerToString(flds []*NestedInteger) string {
	resultStr := ""
	for _, ni := range flds {
		resultStr += (*ni).ToString()
	}
	return resultStr
}

func getNestedIterator(listNestedInteger []*NestedInteger) []int {
	var result []int
	ni := Constructor(listNestedInteger)
	for ni.HasNext() {
		result = append(result, ni.Next())
	}
	return result
}
