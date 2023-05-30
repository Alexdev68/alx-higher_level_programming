#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

        if type(self.__data) != int:
            raise TypeError("data must be an integer")
        if self.__next_node is not None and type(self.__next_node) != Node:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

        if type(self.__data) != int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value

        if self.__next_node is not None and type(self.__next_node) != Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
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
        result = ""
        current = self.__head

        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += "\n"
            current = current.next_node

        return result
