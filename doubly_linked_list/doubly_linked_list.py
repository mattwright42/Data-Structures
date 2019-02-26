"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        current_head = self.head
        if not current_head:
            self.head = ListNode(value)
        else:
            current_head.insert_before(value)
            self.head = current_head.prev

    def remove_from_head(self):
        # no elements in the list
        if not self.head:
            return None
        # single element in the list
        if self.head == self.tail:
            self.head.delete()
            return None
        # multiple elements
        else:
            # create reference to head
            head = self.head
            # run delete
            self.head.delete()
            # return head.value
            return head.value

    def add_to_tail(self, value):
        current_tail = self.tail
        if not current_tail:
            self.tail = ListNode(value)
        else:
            current_tail.insert_after(value)
            self.tail = current_tail.next

    def remove_from_tail(self):
        # no elements in the list
        if not self.tail:
            return None
        # single element in the list
        if self.head == self.tail:
            self.tail.delete()
            return None
        # multiple elements
        else:
            # create reference to tail
            tail = self.tail
            # run delete
            self.tail.delete()
            # return tail.value
            return tail.value

    def move_to_front(self, node):
        # check if the nodelist is empty
        if self.head is not node:
            if node.next and node.prev:  # if in a middle spot
                node.delete()
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    def move_to_end(self, node):
        # check if the nodelist is empty
        if self.tail is not node:
            if node.next and node.prev:  # if in a middle spot
                node.delete()
            current_tail = self.tail
            self.tail = node
            node.prev = current_tail
            current_tail.next = node

    def delete(self, node):
        if node.next is None and node.prev is not None:
            node.prev.next = None
            self.tail = node.prev
            return node.value
        if node.prev is None and node.next is not None:
            node.next.prev = None
            self.head = node.next
            return node.value
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
            return node.value
        else:
            node.delete()

            if node == self.head:
                self.head = node.next
            if node == self.tail:
                self.tail = node.prev
        return node.value

    def get_max(self):
        # store max value in a variable
        max = 0
        current = self.head
        # if list is empty
        # return None
        if not self.head:
            return None
        # if list has only one item
            # return item
        if self.head == self.tail:
            return self.head.value

        while current:
            if current.value > max:
                max = current.value
            current = current.next
        # else
        # compare the current element to the current element's `next` attribute
            # if current element is > max value, current element is new max value
        # return max value
        return max
