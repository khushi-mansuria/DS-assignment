class List:
    def __init__(self):
        self.data = [1, 2, 3, 4]
        print("Original list", self.data)

    def empty(self):
        if len(self.data) == 0:
            return 0
        else:
            return 1

    def popfirst(self):
        if len(self.data) == 0:
            print("Empty")
        else:
            print("First element", self.data[0])

            self.data.pop(0)
            print("Removed first element", self.data)

    def poplast(self):
        if len(self.data) == 0:
            print("Empty")
        else:
            print("Last element", self.data[-1])

            self.data.pop(-1)
            print("Removed last element", self.data)

    def addfirst(self, e):
        self.data.insert(0, e)
        print("Adding first element", self.data)

    def addlast(self, e):
        self.data.append(e)
        print("Adding last element", self.data)


d = List()
d.empty()
d.popfirst()
d.poplast()
d.addfirst(5)
d.addlast(6)
