#!usr/bin/env python

''' Program: BST_class.py
    Author: Matomo Nakamura

    Program behavior: get value and left and right node
'''

class BST:
    def __init__(self, val):
        self.val = val
        self.pointer = None
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_pointer(self):
        return self.pointer

    def get_val(self):
        return self.val

    def set_pointer(self, ptr):
        self.pointer = ptr

    def set_right(self, val):
        self.right = val

    def set_left(self, val):
        self.left = val

    def search(self, val):
        # end if finds the value
        if self.val == val:
            return self
        else:
            if self.right == None:
                rchild = None
            else:
                # finds right childs
                rchild = self.right.search(val)
            if self.left == None:
                lchild = None
            else:
                # finds ledt childs
                lchild = self.left.search(val)
            if rchild != None:
                return rchild
            elif lchild != None:
                return lchild
        return None

    def insert(self, node):
        temp = self
        while temp != None:
            # if value is smaller
            if node.val < temp.val:
                # if node after temp is None
                # create new node
                if temp.left == None:
                    temp.left = node
                    return
                # proceed to next left child
                temp = temp.left
            # if value is greater
            elif node.val > temp.val:
                # if next right node is None
                if temp.right == None:
                    # create new node
                    temp.right = node
                    return
                # proceed to next right child
                temp = temp.right
            else:
                return

    def find_family_root(self):
        if self.pointer.get_parent() == None:
            return self.pointer

        else:
            if self.right == None:
                rchild = None
            else:
                # finds right childs
                rchild = self.right.find_family_root()
            if self.left == None:
                lchild = None
            else:
                # finds ledt childs
                lchild = self.left.find_family_root()
            if rchild != None:
                return rchild
            elif lchild != None:
                return lchild
        return None