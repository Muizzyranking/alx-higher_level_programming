#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """Defines a node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the current data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the current next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        current = self.head
        while current.next_node is not None:
            if value < current.next_node.data:
                new.next_node = current.next_node
                current.next_node = new
                return
            current = current.next_node
        current.next_node = new
        return

    def __str__(self):
        """Print the list"""
        values = []
        tmp = self.head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)
