class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.nodes = {}

    def insert(self, parent, child):
        if parent not in self.nodes:
            self.nodes[parent] = Node(parent)
        if child not in self.nodes:
            self.nodes[child] = Node(child)

        parent_node = self.nodes[parent]
        child_node = self.nodes[child]

        if parent_node.left is None:
            parent_node.left = child_node
        elif parent_node.right is None:
            parent_node.right = child_node


def bt(node, info, visited, sheep, wolf, binary_tree):
    if info[node] == 0:
        sheep += 1  # 현재 노드가 양일 경우
    else:
        wolf += 1  # 현재 노드가 늑대일 경우

    if wolf >= sheep:  # 늑대가 양보다 많아지면 탐색 종료
        return 0

    max_sheep = sheep

    # 현재 노드의 자식 노드 탐색
    for child in visited:  # 이미 방문한 노드 집합에서 이동 가능한 노드 탐색
        for next_node in [binary_tree.nodes[child].left, binary_tree.nodes[child].right]:
            if next_node and next_node.val not in visited:
                max_sheep = max(
                    max_sheep,
                    bt(next_node.val, info, visited | {next_node.val}, sheep, wolf, binary_tree),
                )

    return max_sheep


def solution(info, edges):
    binary_tree = BinaryTree()
    info_dict = {k: v for k, v in enumerate(info)}
    for edge in edges:
        p, c = edge
        binary_tree.insert(p, c)
    answer = bt(0, info, {0}, 0, 0, binary_tree)
    return answer
