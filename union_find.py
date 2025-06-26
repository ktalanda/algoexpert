class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    def find(self, value):
        if value not in self.parents:
            return None

        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])

        return self.parents[value]

    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return None

        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        if self.ranks[valueOneRoot] < self.ranks[valueTwoRoot]:
            self.parents[valueOneRoot] = valueTwoRoot
        elif self.ranks[valueOneRoot] > self.ranks[valueTwoRoot]:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.ranks[valueOneRoot] += 1
