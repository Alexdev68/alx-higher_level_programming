#!/usr/bin/python3
"""This Module houses two classes ``Node`` and ``SinglyLinkedList``.
"""


class Node:
    """This class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """The __init__ method.

        Args:
            data(int): This is the value contained in each node.
            next_node(None): This is an indicator to the next node.

        Raises:
            TypeError: If data is not an integer or if next_node is not None
             and it's type is not Node.
        """
        self.__data = data
        self.__next_node = next_node

        if type(self.__data) != int:
            raise TypeError("data must be an integer")
        if self.__next_node is not None and type(self.__next_node) != Node:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Get data.

        Returns:
            int: The data

        Setter.

            Arg:
                value(int): This is what the data is to be set to.

            Raises:
                TypeError: If data is not an integer.
        """
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

        if type(self.__data) != int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get next_node.

        Returns:
            Node: next_node

        Setter.
            
            Arg:
                value(Node): This is what the next_node is to be set to.

            Raises:
                TypeError: If if next_node is not None and it's type is not 
                Node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value

        if self.__next_node is not None and type(self.__next_node) != Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """This class carries out a linked list operation called sorted insert.
    """

    def __init__(self):
        """This is an simple instantiation with self.__head private instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """This inserts nodes in increasing order.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """This is so we are able to print out it's contents.
        """
        result = ""
        current = self.__head

        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += "\n"
            current = current.next_node

        return result
