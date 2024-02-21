# username - complete info
# id1      - 204912810
# name1    - Yaron Jacob
# id2      - 325720258
# name2    - Ariel Berant


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @type value: any
    @param value: data of your node
    """

    # Fixed number of actions, O(1)

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    # Returns a saved field, O(1)

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    # Returns a saved field, O(1)

    def get_right(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    # Returns a saved field, O(1)

    def get_parent(self):
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    # Returns a saved field, O(1)

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    # Returns a saved field, O(1)

    def get_value(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    # Sets a field, O(1)

    def get_height(self):
        return self.height

    """returns the balance factor

        @rtype: int
        @returns: height of the right child - height of left child
    """

    # Subtracts 2 results from O(1) calls, which is O(1)

    def get_balance_factor(self):
        return self.left.height - self.right.height

    """returns the size

        @rtype: int
        @returns: the height of the current node's subtree
    """

    # Returns a saved field, O(1)

    def get_size(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    # Sets a field, O(1)

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    # Sets a field, O(1)

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    # Sets a field, O(1)

    def set_parent(self, node):
        self.parent = node

    """sets key

    @type key: int or None
    @param key: key
    """

    # Sets a field, O(1)

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    # Sets a field, O(1)

    def set_value(self, value):
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    # Sets a field, O(1)

    def set_height(self, h):
        self.height = h

    """sets the size of the node subtree

        @type size: int
        @param size: the height
    """

    def set_size(self, size):
        self.size = size

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    # Returns on condition, checks saved field, O(1)

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

    # Sets one field, O(1)

    def __init__(self):
        self.root = None

    # add your fields here

    """returns the successor

        @rtype: AVLNode
        @returns: the successor of node
    """

    # Returns the node with the smallest key in the tree that is greater than node's key. Does a maximum of height of
    # tree operations, which is log(n).

    def successor(self, node):
        if node.right.is_real_node():
            node = node.right
            while node.left.is_real_node():
                node = node.left
            return node
        if node.parent.left == node:
            return node.parent
        return None

    """returns the height difference

            @rtype: int
            @returns: the height of node1 - height of node2
    """

    # Returns subtraction of 2 O(1) operations, which is O(1)

    def height_difference(self, node1, node2):
        return node1.height - node2.height

    """rotates right A and B, when B,get_left() is A

                @rtype: None
                @returns: None
    """

    # Runs a fixed number of O(1) operations, which is O(1)

    def rotation_right(self, A, B):
        # Moves node between A and B
        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent
        # Replaces B with A in its father's left\right
        if B.parent is not None:
            if B.parent.left == B:
                A.parent.left = A
            else:
                A.parent.right = A
        B.parent = A
        # case where rotating root
        if self.root == B:
            self.root = A
        self.update(B)

    """rotates right A and B, when B.get_right() is A

                    @rtype: None
                    @returns: None
    """

    # Runs a fixed number of O(1) operations, which is O(1)

    def rotation_left(self, A, B):
        # Moves node between A and B
        B.right = A.left
        B.right.parent = B
        A.left = B
        A.parent = B.parent
        # Replaces B with A in its father's left\right
        if B.parent is not None:
            if B.parent.left == B:
                A.parent.left = A
            else:
                A.parent.right = A
        B.parent = A
        # case where rotating root
        if self.root == B:
            self.root = A
        self.update(B)

    """updates size and height of node and its parents

                    @rtype: None
                    @returns: None
    """

    # Runs a maximum of log(n) times,each time with O(1) operations. So, we get a(log(n)) = O(log(n)).

    @staticmethod
    def update(node):
        # updates virtual node
        if not node.is_real_node():
            node.set_size(0)
            node.set_height(-1)
        else:
            # runs for node and its parents
            while node is not None:
                # If node has no initialized children
                if node.left is None and node.right is None:
                    node.size = 1
                    node.height = 0
                # If node has initialized child only on the right, add 1 to its size
                elif node.left is None:
                    node.size = node.right.size + 1
                    node.height = node.right.height + 1
                # If node has initialized child only on the right, add 1 to its size
                elif node.right is None:
                    node.size = node.left.size + 1
                    node.height = node.left.height + 1
                # If node has initialized children, add 1 to their size sum
                else:
                    node.size = node.right.size + node.left.size + 1
                    node.height = max(node.right.height, node.left.height) + 1
                # Progresses to parent of current node
                node = node.parent

    """searches for a AVLNode in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """

    # Goes on worst case the height of the tree(node not found, at lowest node), which is log(n),
    # when n is our tree's size

    def search(self, key):
        def search_recursion(search_key, node):
            if node is None:  # didn't find node
                return None
            if not node.is_real_node():  # key belongs to a virtual node
                return None
            else:
                if node.get_key() == search_key:  # if we find node, return it
                    return node
                elif node.get_key() < search_key:  # if our key is greater than our current node's key
                    return search_recursion(search_key, node.get_right())
                else:  # if our key is smaller than our current node's keys
                    return search_recursion(search_key, node.get_left())

        return search_recursion(key, self.root)  # returns the result of the recursive function

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    # Finds where to insert(at most the height of the tree), and does a fixed number of actions.
    # Updates, goes back up, commits a rotation(fixed number of actions) once on the way to root.
    # Total: log(n) + d + b(log(n)) + c(log(n)) = log(n), when n is our tree's size,
    # b is the number of actions for the rotation, d is the number of actions for insertion, and c the number of actions
    # in every node we go up in update

    def insert(self, key, val):
        if key is None:  # checks validity
            return

        # initialize node
        new_node = AVLNode(key, val)
        new_node.set_height(0)
        new_node.left = AVLNode(None, None)
        new_node.right = AVLNode(None, None)
        new_node.left.parent = new_node
        new_node.right.parent = new_node

        def insert_inner(curr_node, parent, node):
            if not curr_node.is_real_node():  # checks if we "fell off", and inserts on right side of leaf
                if parent.get_key() > node.get_key():
                    parent.set_left(node)
                else:
                    parent.set_right(node)
                node.set_parent(parent)
            else:  # progresses along tree to find right insert placement
                if curr_node.get_key() > node.get_key():
                    insert_inner(curr_node.get_left(), curr_node, node)
                else:
                    insert_inner(curr_node.get_right(), curr_node, node)

        if self.root is None:  # adds node if tree empty
            self.root = new_node
        else:
            if self.root.is_real_node():  # adds node if tree isn't empty
                insert_inner(self.root, None, new_node)
            else:  # adds node if tree empty
                self.root = new_node

        temp = new_node
        rot_cnt = 0
        self.update(new_node)  # updates our node
        while temp is not None:
            height_change = self.height_difference(temp.left, temp.right)  # calculates BF(y)
            if height_change == 2:  # checks if there is an imbalance from right and fixes it
                if self.height_difference(temp.left.left, temp.left.right) == 1:
                    self.rotation_right(temp.left, temp)
                    rot_cnt += 1
                else:
                    self.rotation_left(temp.left.right, temp.left)
                    self.rotation_right(temp.left, temp)
                    rot_cnt += 2
            if height_change == -2:  # checks if there is an imbalance from right and fixes it
                if self.height_difference(temp.right.left, temp.right.right) == -1:
                    self.rotation_left(temp.right, temp)
                    rot_cnt += 1
                else:
                    self.rotation_right(temp.right.left, temp.right)
                    self.rotation_left(temp.right, temp)
                    rot_cnt += 2
            temp = temp.parent  # advances to parent node
        return rot_cnt  # returns total number of rotations

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    # Let as look at the worst case(deleting a node, it has a successor which needs rotations, and rotating everything).
    # Finds where to delete(at most height of the tree), deletes temp(if needed), rotates(O(log(n)) and deletes node.
    # Updates, goes back up, commits a number of rotations(less than log(n)) on the way to root.
    # Total: log(n) + O(log(n)) + O(log(n)) + d + O(log(n)) + c(log(n)) = O(log(n)), when n is our tree's size,
    # d is the number of actions for deletion, and c the number of actions in every node we go up in update.

    def delete(self, node):
        if not node.get_right().is_real_node() or not node.get_left().is_real_node():  # checks if node has children
            if node.get_right().is_real_node():  # checks if node has right child
                node.get_right().set_parent(node.get_parent())
                if node.get_parent() is None:  # special case for root node
                    self.root = node.get_right()
                    return 0
                else:
                    if node.get_parent().get_value() > node.get_value():  # checks side to insert children to parent
                        node.get_parent().set_left(node.get_right())
                    else:
                        node.get_parent().set_right(node.get_right())
            else:  # similar for left, just with possibility of no children
                node.get_left().set_parent(node.get_parent())
                if node.get_parent() is None:  # checks if deleted node is root
                    if not node.get_left().is_real_node():
                        self.root = None
                    else:
                        self.root = node.get_left()
                    return 0
                else:
                    if node.get_parent().get_value() > node.get_value():  # checks side to insert children to parent
                        node.get_parent().set_left(node.get_left())
                    else:
                        node.get_parent().set_right(node.get_left())

            if node.get_parent() is not None:  # configures temp for rotations if needed
                temp = node.get_parent()
            temp_rot = 0

        else:
            # gets and deletes successor, saves the number of rotations it needed
            temp = self.successor(node)
            temp_rot = self.delete(temp)
            # configures the replacement node's parent and children
            temp.set_right(node.get_right())
            temp.get_right().set_parent(temp)
            temp.set_parent(node.get_parent())
            temp.set_left(node.get_left())
            temp.get_left().set_parent(temp)
            if temp.get_parent() is None:  # special case for root
                self.root = temp
            else:
                if temp.get_parent().get_value() > temp.get_value():  # checks side to insert temp to parent
                    temp.get_parent().set_left(temp)
                else:
                    temp.get_parent().set_right(temp)

        # resets node
        node.set_right(None)
        node.set_left(None)
        node.set_parent(None)
        self.update(node)

        return temp_rot + self.fix_rotations(temp)  # returns rotation fixer

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    """

    # Commits two operations(append, condition) for every node, and one more for root.
    # Since we have n nodes, this is done in 2n + 1 = O(n) time.

    def avl_to_array(self):
        avl_array = []   # initializes empty list

        def avl_to_array_inner(node):
            if node.is_real_node():  # checks if we "fell off"
                avl_to_array_inner(node.get_left())  # appends the smaller values
                avl_array.append((node.get_key(), node.get_value()))  # appends current value
                avl_to_array_inner(node.get_right())  # appends greater values

        if self.root is not None:  # checks if tree isn't empty
            avl_to_array_inner(self.root)  # calls array appending function

        return avl_array  # returns the completed array

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    # Returns a saved field, O(1)

    def size(self):
        return self.root.size

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
        if node.key == 3648:
            hi = 5
        left_tree = AVLTree()
        left_tree.root = node.left
        left_tree.root.set_parent(None)
        right_tree = AVLTree()
        right_tree.root = node.right
        right_tree.root.set_parent(None)
        par = node.parent
        while par is not None:
            if par.key < node.key:
                tree = AVLTree()
                tree.root = par.left
                trl = tree.root.left
                trr = tree.root.right
                par.left.set_parent(None)
                tree.join(left_tree, par.key, par.value)
                left_tree.root = tree.root

            else:
                tree = AVLTree()
                tree.root = par.right
                par.right.set_parent(None)
                right_tree.join(tree, par.key, par.value)
            par = par.parent
        if not left_tree.root.is_real_node():
            left_tree.root = None
        if not right_tree.root.is_real_node():
            right_tree.root = None
        return left_tree, right_tree

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separating self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):
        if tree2.root is None:
            self.insert(key, val)
            return self.root.height + 1
        if self.root is None:
            tree2.insert(key, val)
            self.root = tree2.root
            return self.root.height + 1
        if not tree2.root.is_real_node():
            self.insert(key, val)
            return self.root.height + 1
        if not self.root.is_real_node():
            tree2.insert(key, val)
            self.root = tree2.root
            return self.root.height + 1
        res = self.height_difference(self.root, tree2.root) + 1
        if tree2.root.height > self.root.height:
            t1 = AVLTree()
            t2 = tree2
            t1.root = self.root
        else:
            t2 = AVLTree()
            t1 = tree2
            t2.root = self.root
        node = t2.root
        for i in range(t2.root.height):
            if node.height == t1.root.height or node.height == t1.root.height + 1:
                break
            else:
                if t1.root.key < t2.root.key:
                    node = node.left
                else:
                    node = node.right
        if key == 3648:
            hi = 5
        x = AVLNode(key, val)
        if t1.root.key < t2.root.key:
            x.set_left(t1.root)
            x.set_right(node)
        else:
            x.set_left(node)
            x.set_right(t1.root)
        x.set_parent(node.parent)
        x.right.parent = x
        x.left.parent = x
        temp = x.parent
        if temp is None:
            self.root = x
            self.update(x)
            return res
        if temp.right == x.right or temp.right == x.left:
            temp.right = x
        if temp.left == x.right or temp.left == x.left:
            temp.left = x
        self.update(x)
        cur = temp
        while temp is not None:
            height_change = self.height_difference(temp.left, temp.right)
            if height_change == 2:
                if self.height_difference(temp.left.left, temp.left.right) == 1:
                    self.rotation_right(temp.left, temp)
                else:
                    self.rotation_left(temp.left.right, temp.left)
                    self.rotation_right(temp.left, temp)
            if height_change == -2:
                if self.height_difference(temp.right.left, temp.right.right) == -1:
                    self.rotation_left(temp.right, temp)
                else:
                    self.rotation_right(temp.right.left, temp.right)
                    self.rotation_left(temp.right, temp)
            cur = temp
            temp = temp.parent
        self.root = cur
        return res

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    # Returns a saved field, O(1)

    def get_root(self):
        return self.root

    # Updates node(a fixed number of actions for at most log(n) times), and commits at most log(n) rotations, with every
    # one taking a fixed number of actions. Takes at most a(log(n)) + b(log(n)) = O(log(n)).

    def fix_rotations(self, node):
        rot_cnt = 0  # rotation counter
        self.update(node)  # updates our current node
        while node is not None:
            height_change = self.height_difference(node.left, node.right)  # calculates BF(y)
            if height_change == 2:  # checks if there is an imbalance from right and fixes it
                if self.height_difference(node.left.left, node.left.right) == -1:
                    self.rotation_left(node.left.right, node.left)
                    self.rotation_right(node.left, node)
                    rot_cnt += 2
                else:
                    self.rotation_right(node.left, node)
                    rot_cnt += 1
            if height_change == -2:  # checks if there is an imbalance from left and fixes it
                if self.height_difference(node.right.left, node.right.right) == 1:
                    self.rotation_right(node.right.left, node.right)
                    self.rotation_left(node.right, node)
                    rot_cnt += 2
                else:
                    self.rotation_left(node.right, node)
                    rot_cnt += 1
            node = node.parent  # advances to parent node
        return rot_cnt  # returns total number of rotations


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        print_tree(node.right, level + 1)
