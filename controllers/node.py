class Node:
    def __init__(self, pos, heuristic):
        self.pos = pos
        self.heuristic = heuristic
        self.children = []

    def append_child(self, child):
        self.children.append(child)

