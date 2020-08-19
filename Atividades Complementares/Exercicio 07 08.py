#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Engenharia da Coomputação
# Aluno:Jose Arlindo 

class Node(object):
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def add(self, key, value):
        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return None

        for i, item in enumerate(self.keys):
            if key == item:
                self.values[i].append(value)
                break

            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break

            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])

    def split(self):

        left = Node(self.order)
        right = Node(self.order)
        mid = self.order // 2

        left.keys = self.keys[:mid]
        left.values = self.values[:mid]

        right.keys = self.keys[mid:]
        right.values = self.values[mid:]


        self.keys = [right.keys[0]]
        self.values = [left, right]
        self.leaf = False

    def is_full(self):
        return len(self.keys) == self.order

    def show(self, counter=0):

        print(counter, str(self.keys))

        if not self.leaf:
            for item in self.values:
                item.show(counter + 1)

class BPlusTree(object):

    def __init__(self, order=8):
        self.root = Node(order)

    def _find(self, node, key):

        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def _merge(self, parent, child, index):

        parent.values.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insert(self, key, value):

        parent = None
        child = self.root

        while not child.leaf:
            parent = child
            child, index = self._find(child, key)

        child.add(key, value)

        if child.is_full():
            child.split()

            if parent and not parent.is_full():
                self._merge(parent, child, index)

    def retrieve(self, key):
        child = self.root

        while not child.leaf:
            child, index = self._find(child, key)

        for i, item in enumerate(child.keys):
            if key == item:
                return child.values[i]

        return None

    def show(self):
        self.root.show()

def demo_bplustree():
    print('Inicializando Árvore B+...')
    bplustree = BPlusTree(order=4)

    print('\nÁrvore B+ com 1 item...')
    bplustree.insert('a', 'alpha')
    bplustree.show()

    print('\nÁrvore B+ com 2 items...')
    bplustree.insert('b', 'bravo')
    bplustree.show()

    print('\nÁrvore B+ com 3 items...')
    bplustree.insert('c', 'charlie')
    bplustree.show()

    print('\nÁrvore B+ com 4 items...')
    bplustree.insert('d', 'delta')
    bplustree.show()

    print('\nÁrvore B+ com 5 items...')
    bplustree.insert('e', 'echo')
    bplustree.show()

    print('\nÁrvore B+ com 6 items...')
    bplustree.insert('f', 'foxtrot')
    bplustree.show()

    print('\nRetornando valores da chave e...')
    print(bplustree.retrieve('e'))
    
    print('\nRetornando valores da chave f...')
    print(bplustree.retrieve('f'))

if __name__ == '__main__':
    print('\n')
    demo_bplustree()


# In[ ]:

