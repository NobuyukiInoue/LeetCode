/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

package solution

import "strconv"

type NestedInteger struct {
	Val  *int
	List [](*NestedInteger)
}

func (this NestedInteger) IsInteger() bool {
	return this.Val != nil
}

func (this NestedInteger) GetInteger() int {
	return *(this.Val)
}

func (this *NestedInteger) SetInteger(value int) {
	*(this.Val) = value
}

func (this *NestedInteger) Add(elem NestedInteger) {
	if (*this).List != nil {
		(*this).List = append((*this).List, &elem)
	} else {
		(*this).List = make([](*NestedInteger), 0)
		(*this).List = append((*this).List, &elem)
	}
}

func (this *NestedInteger) GetList() [](*NestedInteger) {
	return (*this).List
}

func (this *NestedInteger) ToString() string {
	resultStr := ""
	if (*this).IsInteger() {
		resultStr += strconv.Itoa(*((*this).Val))
	}
	if (*this).List != nil {
		if len(resultStr) > 0 {
			resultStr += ","
		}
		resultStr += "["
		for _, ni := range (*this).List {
			if ni.IsInteger() {
				if resultStr[len(resultStr)-1] != '[' {
					resultStr += "," + strconv.Itoa(*(ni.Val))
				} else {
					resultStr += strconv.Itoa(*(ni.Val))
				}
			} else {
				if resultStr[len(resultStr)-1] != '[' {
					resultStr += "," + ni.ToString()
				} else {
					resultStr += ni.ToString()
				}
			}
		}
		resultStr += "]"
	}
	return resultStr
}
