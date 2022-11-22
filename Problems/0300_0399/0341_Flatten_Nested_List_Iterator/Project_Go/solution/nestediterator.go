package solution

// 5ms - 10ms

type NestedIterator struct {
	intList []int
	index   int
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	ni := NestedIterator{}
	for _, nestedInteger := range nestedList {
		flatten(&ni, nestedInteger)
	}
	return &ni
}

func flatten(ni *NestedIterator, nested *NestedInteger) {
	if (*nested).IsInteger() {
		(*ni).intList = append((*ni).intList, nested.GetInteger())
	} else {
		for _, nestedFromList := range (*nested).GetList() {
			flatten(ni, nestedFromList)
		}
	}
}
func (this *NestedIterator) Next() int {
	(*this).index++
	return (*this).intList[(*this).index-1]
}

func (this *NestedIterator) HasNext() bool {
	return (*this).index < len((*this).intList)
}
