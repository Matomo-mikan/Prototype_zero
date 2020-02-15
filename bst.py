#!usr/bin/env python

class TreeNode():
    # constructor
    def __init__(self, value):
        self._value = value
        self._lchild = None
        self._rchild = None

    # insert node with value by evaluating
    def insert(self, n):
        if n > self._value:
            if self._rchild == None:
                self._rchild = TreeNode(n)
            else:
                insert(self._rchild, n)
        else:
            if self._lchild == None:
                self._lchild = TreeNode(n)
            else:
                insert(self._lchild, n)
        return self

    '''
    Iterate through until it finds None
    to return list, otherwhise it returns
    the node every time.
    '''
    def path(self, n):
        # base case return list
        if self._value == n:
            return [n]
        elif n > self._value:
            if self._rchild == None:
                return None
            else:
                new = self._rchild.path(n)
        elif n < self._value:
            if self._lchild == None:
                return None
            else:
                new = self._lchild.path(n)
        if new == None:
            return None
        else:
            return [self._value] + new

def mktree(node_list):
    if node_list == []:
        return None
    else:
        # construct the head node given by tree
        tree = TreeNode(node_list[0])
        # connect nodes after head node
        for i in range(1, len(node_list)):
            insert(tree, node_list[i])
    return tree

def insert(tree, val):
    if tree == None:
        return TreeNode(val)
    else:
        # implement if tree is not None
        return tree.insert(val)

def path(tree, val):
    if tree == None:
        return None
    else:
        # pass value to path
        return tree.path(val)

def lca(tree, val1, val2):
    # these paths are list
    path1 = path(tree, val1)
    path2 = path(tree, val2)
    if path1 == None or path2 == None:
        return None
    else:
        return helper(path1, path2)

def helper(list1, list2):
    # base case
    if len(list1) == 0:
        return None
    lst = list1[-1]
    # this will check same value
    if lst in list2:
        return lst
    else:
        return helper(list1[:-1], list2)