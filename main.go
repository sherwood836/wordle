package main

import (
	"fmt"
	"sort"
)

type Pair struct {
	a int
	b int
}

func Less(i, j Pair) bool {
	return i.a < j.a
}

func Len(i, j Pair) bool {
	return i.a < j.a
}

func main() {

	pair1 := Pair{10, 30}
	pair2 := Pair{50, 65}
	pair3 := Pair{65, 80}
	pair4 := Pair{85, 100}
	// pair5 := Pair{35, 55}
	// pair6 := Pair{35, 85}
	// pair7 := Pair{15, 20}
	// pair8 := Pair{25, 26}
	// pair9 := Pair{26, 30}
	// pair10 := Pair{27, 30}

	fmt.Println(find_chain([]Pair{pair1}))
	fmt.Println(find_chain([]Pair{pair1, pair2}))
	fmt.Println(find_chain([]Pair{}))
	fmt.Println(find_chain([]Pair{pair1, pair2, pair3, pair4}))

}

func find_chain(arr []Pair) int {
	sort.Slice(arr, func(i, j int) bool {
		return arr[i].a < arr[j].a
	})

	var final_list []Pair = []Pair{}

	if len(arr) > 0 {
		final_list = append(final_list, arr[0])

		if len(arr) > 1 {
			for idx := 1; idx < len(arr); idx++ {
				if final_list[len(final_list)-1].b < arr[idx].a {
					final_list = append(final_list, arr[idx])
				} else if final_list[len(final_list)-1].b > arr[idx].b {
					final_list = final_list[:len(final_list)-1]
					final_list = append(final_list, arr[idx])
				}
			}
		}
	}

	return len(final_list)
}
