package solution

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
	"time"
	"unicode"
)

var BUSINESS_LINE_ORDERED_BY_SORTING_PRIORIITY = []string{"electronics", "grocery", "pharmacy", "restaurant"}

// 1ms
func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
	var businessLineToCodes map[string][]string = createBusinessLineToCodes(code, businessLine, isActive)
	return createSortedValidCoupons(businessLineToCodes)
}

func createBusinessLineToCodes(code []string, businessLine []string, isActive []bool) map[string][]string {
	businessLineToCodes := map[string][]string{}
	for i := range code {
		if isValidCode(code[i]) && isValidBusinessLine(businessLine[i]) && isActive[i] {
			if _, has := businessLineToCodes[businessLine[i]]; !has {
				businessLineToCodes[businessLine[i]] = []string{}
			}
			businessLineToCodes[businessLine[i]] = append(businessLineToCodes[businessLine[i]], code[i])
		}
	}
	return businessLineToCodes
}

func isValidCode(code string) bool {
	for _, current := range code {
		if !unicode.IsLetter(current) && !unicode.IsDigit(current) && current != '_' {
			return false
		}
	}
	return len(code) > 0
}

func isValidBusinessLine(businessLine string) bool {
	return businessLine == "electronics" ||
		businessLine == "grocery" ||
		businessLine == "pharmacy" ||
		businessLine == "restaurant"
}

func createSortedValidCoupons(businessLineToCodes map[string][]string) []string {
	sortedValidCoupons := []string{}

	for _, businessLine := range BUSINESS_LINE_ORDERED_BY_SORTING_PRIORIITY {
		if _, has := businessLineToCodes[businessLine]; !has {
			continue
		}
		slices.Sort(businessLineToCodes[businessLine])
		for _, code := range businessLineToCodes[businessLine] {
			sortedValidCoupons = append(sortedValidCoupons, code)
		}
	}
	return sortedValidCoupons
}

func StringArrayToBoolString(flds []string) []bool {
	res := make([]bool, len(flds))
	for i, fld := range flds {
		if fld == "true" {
			res[i] = true
		} else {
			res[i] = false
		}
	}
	return res
}

func BoolArrayToString(flds []bool) string {
	res := "["
	for i := 0; i < len(flds); i++ {
		res += ", " + strconv.FormatBool(flds[i])
	}
	return res + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	code := strings.Split(flds[0], ",")
	businessLine := strings.Split(flds[1], ",")
	isActive := StringArrayToBoolString(strings.Split(flds[2], ","))
	fmt.Printf("code = [%s], buisinessLine = [%s], isActive = [%s]\n", StringArrayToString(code), StringArrayToString(businessLine), BoolArrayToString(isActive))

	timeStart := time.Now()

	result := validateCoupons(code, businessLine, isActive)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
