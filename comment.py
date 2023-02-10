'''
CommentNode
    comment
    parent
    children_list
'''
from __future__ import annotations

class Comment:
    id: str

class CommentNode:
    comment: Comment
    parent: CommentNode
    children_list: list[CommentNode]

    def __init__(self, comment: Comment):
        self.comment = comment
        self.parent = None
        self.children_list = []

def build_tree(comment_list):
    lookup_map = {}
    return_list = []

    for comment in comment_list:
        this_comment = Comment()
        this_comment.id = comment[0]
        new_node = CommentNode(this_comment)
        lookup_map[comment[0]] = new_node

        if not comment[1]:
            return_list.append(new_node)

    for comment in comment_list:
        if comment[1]:
            this_list = lookup_map[comment[1]].children_list or []
            this_list.append(lookup_map[comment[0]])
            lookup_map[comment[1]].children_list = this_list
            lookup_map[comment[0]].parent = lookup_map[comment[1]]
    
    return return_list


def print_tree(comment_node_list):
    for comment_node in comment_node_list:
        print_node(comment_node, 0) 

def print_node(node, level):
    print("\t"*level, node.comment.id)

    for child in node.children_list:
        print_node(child, level + 1)


comment_list = [("1", None),
                ("2", None),
                ("3", None),
                ("4", "1"),
                ("5", "1"),
                ("6", "4"),
                ("7", "5"),
                ("8", "7"),
                ]

print(build_tree(comment_list))
print_tree(build_tree(comment_list))
