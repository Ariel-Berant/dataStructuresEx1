# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.key is None:
            return False
        return True


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.size = 0

    # add your fields here

    """searches for a AVLNode in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """

    def succsessor(node):
        if node.right.is_real_node():
            node = node.right
            while node.left.is_real_node():
                node = node.left
            return node
        if node.parent.left == node:
            return node.parent
        return None

    def predecessor(self, node):
        if node.left.is_real_node():
            node = node.left
            while node.right.is_real_node():
                node = node.right
            return node
        if node.parent.right == node:
            return node.parent
        return None

    def height_difference(self, node1, node2):
        return abs(node1.height - node2.height)

    def rotation_right(self, A, B):
        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent
        if B.parent.left == B:
            A.parent.left = A
        else:
            A.parent.right = A
        B.parent = A
        if self.root == B:
            self.root = A

    def rotation_left(self, A, B):
        B.right = A.left
        B.right.parent = B
        A.left = B
        A.parent = B.parent
        if B.parent.left == B:
            A.parent.left = A
        else:
            A.parent.right = A
        B.parent = A
        if self.root == B:
            self.root = A

    def search(self, key):
        def search_recursion(search_key, node):
            if node is None:
                return None
            else:
                if node.get_key() == search_key:
                    return node
                elif node.get_height() < search_key:
                    return search_recursion(search_key, node.get_right())
                else:
                    return search_recursion(search_key, node.get_left())

        return search_recursion(key, self.root)

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        new_node = AVLNode(key, val)
        new_node.set_height(0)

        def insert_inner(curr_node, parent, node):
            if curr_node is None:
                if parent.get_key() < node.get_key():
                    parent.set_left(node)
                else:
                    parent.set_right(node)
                node.set_parent(parent)
            else:
                curr_node.set_height(curr_node.get_height() + 1)
                if curr_node.get_key() > node.get_key():
                    insert_inner(curr_node.get_left(), curr_node, node)
                else:
                    insert_inner(curr_node.get_right(), curr_node, node)

        if self.size == 0:
            self.root = new_node
        else:
            insert_inner(self.root, None, new_node)

        return -1

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        return -1

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        avl_array = []

        def avl_to_array_inner(node):
            if node is not None:
                avl_to_array_inner(node.get_left())
                avl_array.append((node.get_key(), node.get_val()))
                avl_to_array_inner(node.get_right())

        avl_to_array_inner(self.root)

        return avl_array

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.size

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):
        self.size = self.size + tree2.size + 1
        res = self.height_difference(self.root, tree2.root) + 1
        if tree2.root.height > self.root.height:
            t2 = tree2
            t1 = self
        else:
            t1 = tree2
            t2 = self
        node = t2.root
        for i in range(t2.root.height):
            if node.height == t1.root.height:
                break
            else:
                if node.left.height > node.right.height:
                    node = node.left
                else:
                    node = node.right
        x = AVLNode(key, val)
        if t1.root.key < t2.root.key:
            x.set_left(t1.root)
            x.set_right(t2.root)
        else:
            x.set_left(t2.root)
            x.set_right(t1.root)
        x.set_height = t1.root + 1
        x.set_parent = node.parent
        temp = x.parent
        while temp is not None:
            temp.height += 1
            temp = temp.parent
        height_change = self.height_difference(x.parent.left, x.parent.right)
        if height_change == 2:
            if self.height_difference(x.left, x.right) == 1:
                self.rotation_right(x.left, x)
            else:
                self.rotation_left(x.left.right, x.left)
                self.rotation_right(x.left, x)
        if height_change == -2:
            if self.height_difference(x.left, x.right) == -1:
                self.rotation_left(x.right, x)
            else:
                self.rotation_left(x.right.left, x.right)
                self.rotation_right(x.right, x)
        self.root = temp
        return res

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root
