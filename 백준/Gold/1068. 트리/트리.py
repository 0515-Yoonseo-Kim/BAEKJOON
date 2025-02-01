class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Tree:
    def __init__(self, remove_node):
        self.root = None
        self.nodes = dict()
        self.removed_node = {remove_node}

    def insert(self, parent, child):
        if parent in self.removed_node or child in self.removed_node:
            self.removed_node.add(child)
            return

        if child not in self.nodes:
            new_node = Node(child)
            self.nodes[child] = new_node
        else:
            new_node = self.nodes[child]

        if parent == -1:
            self.root = new_node
            return
        if parent not in self.nodes:
            self.nodes[parent] = Node(parent)

        parent_node = self.nodes[parent]
        parent_node.children.append(new_node)

    def get_leaf_nodes(self, node):
        if node is None:
            return 0
        
        if not node.children:
            return 1
        
        return sum(self.get_leaf_nodes(child) for child in node.children)

if __name__ == "__main__":
    N = int(input())  # 노드 개수
    tree_info = list(map(int, input().split()))
    remove_node = int(input())

    tree = Tree(remove_node)

    for child, parent in enumerate(tree_info):
        tree.insert(parent, child)

    if tree.root is None:
        print(0)
    else:
        print(tree.get_leaf_nodes(tree.root))
