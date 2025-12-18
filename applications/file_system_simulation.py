class FileNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def display(self, level=0):
        print("   " * level + ("[File] " if self.is_file else "[Folder] ") + self.name)
        for child in self.children:
            child.display(level + 1)

if __name__ == "__main__":
    root = FileNode("C:")
    docs = FileNode("Documents")
    pics = FileNode("Pictures")
    file1 = FileNode("invoice.pdf", True)

    root.add_child(docs)
    root.add_child(pics)
    docs.add_child(file1)

    root.display()
