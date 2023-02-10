package main

// run this with "go run find_chain.go"
import (
	"fmt"
)

type Comment struct {
	id      string
	comment string
}

type CommentNode struct {
	comment       Comment
	parent        *CommentNode
	children_list []*CommentNode
}

type Pair struct {
	a Comment
	b string
}

func main() {

	pair1 := Pair{Comment{id: "1"}, ""}
	pair2 := Pair{Comment{id: "2"}, ""}
	pair3 := Pair{Comment{id: "3"}, ""}
	pair4 := Pair{Comment{id: "4"}, "1"}
	pair5 := Pair{Comment{id: "5"}, "1"}
	pair6 := Pair{Comment{id: "6"}, "4"}
	pair7 := Pair{Comment{id: "7"}, "5"}

	fmt.Println(build_tree([]Pair{pair1, pair2, pair3, pair4, pair5, pair6, pair7}))
	print_tree(build_tree([]Pair{pair1, pair2, pair3, pair4, pair5, pair6, pair7}))
}

func build_tree(arr []Pair) []CommentNode {
	var final_list []CommentNode = []CommentNode{}
	var node_lookup = make(map[string]*CommentNode)

	for idx := 0; idx < len(arr); idx++ {
		var this_node CommentNode = CommentNode{comment: arr[idx].a}
		this_node.comment = arr[idx].a
		node_lookup[arr[idx].a.id] = &this_node
	}

	for idx := 0; idx < len(arr); idx++ {
		var this_node = node_lookup[arr[idx].a.id]

		if arr[idx].b != "" {
			var parent_node = node_lookup[arr[idx].b]

			this_node.parent = parent_node
			parent_node.children_list = append(parent_node.children_list, this_node)
			node_lookup[arr[idx].b] = parent_node
		}
	}

	for idx := 0; idx < len(arr); idx++ {
		if arr[idx].b == "" {
			final_list = append(final_list, *node_lookup[arr[idx].a.id])
		}
	}

	return final_list
}

func print_tree(arr []CommentNode) {
	for idx := 0; idx < len(arr); idx++ {
		print_node(arr[idx], 0)
	}
}

func print_node(node CommentNode, level int) {
	for idx := 0; idx < level; idx++ {
		fmt.Print("\t")
	}

	fmt.Println(node.comment.id)

	for idx := 0; idx < len(node.children_list); idx++ {
		print_node(*node.children_list[idx], level+1)
	}
}
