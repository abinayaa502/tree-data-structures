class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node
    def search(self, value):
        return self._search_recursive(self.root, value)
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node     
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

if __name__ == "__main__":
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        bst.insert(v)

    print("Inorder Traversal (sorted): ")
    bst.inorder(bst.root)

    print("\nSearch 40: ", "Found" if bst.search(40) else "Not Found")
    print("Search 90: ", "Found" if bst.search(90) else "Not Found")
