class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        given = value
        complete = False
        while not complete:
            if given < current.value:
                # add value to the left node
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree(given)
                    complete = True
            if given > current.value:
                # add value to the right node
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTree(given)
                    complete = True

    def contains(self, target):
        current = self
        complete = False
        while not complete:
            # if there is nothing left to check, return False
            if not current:
                return False
            # if the value of the current node is == target
            if current.value == target:
                return True
            # if the current value is greater than the target
            elif current.value > target:
                current = current.left
            # if current value is less than the target
            else:
                current = current.right

    def get_max(self):
        current = self
        max = 0
        while current:
          # if the current value is greater than the mx
            if current.value > max:
                max = current.value
                current = current.right

        return max


# contains
# search the BST for the given target value, returning a boolean

# base case #1: we've found the value we're looking for
# check if the target value matches self.value on the current node
# if target. == self.value:
    # if so, return True
    # return True
# compare the target value against self.value
    # if target < self.value
    # if target < self.value:
        # if self.left exists
        # if self.left:
        # call the left child's contains method, passing in the target value
        # return self.left.contains(target)

        # base case #2: we know that the target value should be in the left subtree
        # but there's no left subtree
        # else, return False
        # else:
        # return False

    # if target >= self.value
    # if target >= self.value
       # if self.right exists
       # if self.right:
        # call the right child's contains method, passing in the target value
        # return self.right.contains(target)

        # base case 3: we know that the target value should be in the right subtree
        # but there's no right subtree
        # else, return False
        # else:
        # return False
