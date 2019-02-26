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
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def move_to_end(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def delete(self, node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):

        if not self.head:
            return None
        current_node = self.head
        max_value = current_node.value
        while current_node.next:
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value
